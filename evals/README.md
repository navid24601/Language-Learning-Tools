# Manual evaluation

Each skill’s `cases.json` includes positive, negative and multi-turn cases. Record date, host, model, package version, invocation, transcript and evidence for each check.

1. **Discovery:** In a fresh session with the plugin enabled, send the first user turn without naming a skill. Record whether the target skill is selected if the host exposes this; otherwise mark activation unknown. Negative cases check that the target is not selected; another relevant skill may be appropriate.
2. **Behavior:** For positive cases, start another fresh session, explicitly invoke the target skill, then send each subsequent turn in order. Do not show the checks to the agent. Judge each check pass, fail or unknown. Evaluate negative cases through the ordinary discovery response, not by forcing the target skill.
3. **Grade:** Allow defensible language and regional alternatives. A material linguistic error, invented capability or history, unwanted answer disclosure in a quiz, altered meaning in editing or translation, or pronunciation assessment from text is a critical failure. Optional scoring is described in the [rubric](vocabulary/rubric.md); mark irrelevant dimensions N/A.
4. Record failures and re-run affected cases and representative regressions after changes. Where practical, compare with a no-skill baseline. These observations do not measure learning gains.
