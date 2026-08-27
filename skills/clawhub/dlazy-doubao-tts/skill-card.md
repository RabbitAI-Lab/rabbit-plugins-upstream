## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to turn text prompts into Doubao TTS speech through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts are sent to the dLazy/Doubao hosted API for inference.

Mitigation: Do not submit sensitive text unless the user accepts that hosted API processing.

Risk: The dLazy CLI can persist an API key after authentication.

Mitigation: Use per-run DLAZY_API_KEY when a saved credential is not desired, and rotate or revoke keys from the provider dashboard when needed.

Risk: Generic text-to-speech requests could be routed through this third-party provider unintentionally.

Mitigation: Confirm the provider choice before using the skill for generic TTS tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Files]

**Output Format:** [Markdown guidance with bash commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted result URLs or saved local assets; async runs return a generateId and status for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
