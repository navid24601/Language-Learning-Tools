from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("vocabulary", "grammar", "writing", "speaking", "translator")
errors = []
def check(condition, message):
    if not condition: errors.append(message)

try:
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    check(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "portable schema missing")
    check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest.get("name", ""))), "invalid plugin name")
    check(bool(re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", manifest.get("version", ""))), "invalid version")
except (OSError, ValueError) as exc: errors.append(f"manifest: {exc}")

total = 0
for name in SKILLS:
    skill = ROOT / "skills" / name / "SKILL.md"
    try:
        text = skill.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        check(len(parts) == 3 and not parts[0].strip(), f"{name}: frontmatter missing")
        if len(parts) == 3:
            check(bool(re.search(rf"(?m)^name: {name}$", parts[1])), f"{name}: name mismatch")
            desc = re.search(r"(?m)^description: (.+)$", parts[1])
            check(bool(desc) and len(desc.group(1)) <= 1024, f"{name}: invalid description")
        refs = re.findall(r"\]\((references/[^)#]+)(?:#[^)]*)?\)", text)
        check(bool(refs), f"{name}: no references linked")
        for ref in refs:
            target = (skill.parent / ref).resolve()
            check(target.is_relative_to(skill.parent.resolve()) and target.is_file(), f"{name}: invalid reference {ref}")
        for ref in (skill.parent / "references").glob("*.md"):
            check(f"references/{ref.name}" in refs, f"{name}: unlinked reference {ref.name}")
    except OSError as exc: errors.append(f"{name}: {exc}")
    try:
        cases = json.loads((ROOT / "evals" / name / "cases.json").read_text(encoding="utf-8"))
        ids = [c["id"] for c in cases]
        check(len(cases) >= 8 and len(ids) == len(set(ids)), f"{name}: invalid case count or IDs")
        check(any(not c["activation_expected"] for c in cases), f"{name}: missing negative case")
        check(any(len(c["turns"]) > 1 for c in cases), f"{name}: missing multi-turn case")
        for c in cases:
            check(isinstance(c["activation_expected"], bool) and bool(c["turns"]), f"{name}: invalid case {c['id']}")
            for turn in c["turns"]: check(bool(turn.get("user")) and bool(turn.get("checks")), f"{name}: invalid turn {c['id']}")
        total += len(cases)
    except (OSError, ValueError, KeyError, TypeError) as exc: errors.append(f"{name} cases: {exc}")
if errors:
    print("FAIL\n" + "\n".join(errors)); sys.exit(1)
print(f"PASS: manifest, {len(SKILLS)} skills and references, {total} evaluation cases structurally valid")
