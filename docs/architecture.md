# Architecture and decisions

Verified against official documentation on 2026-10-31: [package plugins](https://developers.openai.com/plugins/build/plugins), [build skills](https://developers.openai.com/plugins/build/skills), and [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

## Contract

A portable plugin has root `plugin.json` with the Agent Plugins schema and stable kebab-case identity. Its root `skills/` contains skill directories with `SKILL.md`; name and description frontmatter enable discovery. References are optional and loaded selectively. A compatibility `.codex-plugin/plugin.json` is optional; do not add a duplicate manifest without a tested need. A marketplace is separate from the package. No MCP or backend is needed for these skills. Naming is `language-learning-tools` for the machine identifier and Language-Learning-Tools for the working display name. Version the package as a whole for now; individual versioning is deferred.

## Design review

- A mandatory ten-step lesson would frustrate brief requests. Route by intent; make practice optional unless requested.
- CEFR is an approximate aid, not a diagnosis or a property that can reliably be inferred from one sentence. Respect stated level and preferences; default to accessible language and adapt.
- Examples and collocations can sound plausible but be wrong or unusual. Mark uncertainty, avoid invented frequency claims, and check authoritative sources where necessary and available.
- Shared files outside a skill are brittle when copied independently. Put operational teaching rules inside each skill; the project principles guide authors rather than serving as a runtime dependency. Accept some deliberate duplication.
- Retrieval and spaced review are learning opportunities, not proof of mastery. No claims of tracking or scheduling without a real capability. Test delayed outcomes separately in future.
- Overlapping skills can misroute. Descriptions state primary intent; ordinary translation, editing, and general conversation should not automatically become vocabulary lessons. Test collisions after the other skills exist.
- A weighted score can conceal a serious error. The rubric has critical failures and intent-specific non-applicable criteria; it is an observational review, not a learning measure.

## Decisions still conditional

Codex is the first local test target; the portable package is designed for broader use, but ChatGPT installation and actual discovery remain to be tested. Language preferences are conversational, not global configuration. Quick, deep and quiz are routing choices rather than rigid commands. Adopt a framework only after repeatable manual baselines justify it. Publishing, integrations, persistence and learner data are future decisions.
