## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to turn text prompts into Doubao TTS speech through the dLazy CLI and hosted API. It is suited for generating narration, voice broadcasts, and other text-to-speech assets where sending prompt text to dLazy is acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompt text and selected parameters to dLazy's hosted API for processing.

Mitigation: Avoid sending sensitive text unless the user intends it to be processed by dLazy and is comfortable with that service boundary.

Risk: The dLazy API key is required for use and may be stored in local CLI configuration.

Mitigation: Treat the API key as a secret, prefer per-session environment variables on shared machines, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Local media paths supplied to dLazy CLI commands may be uploaded to dLazy file storage.

Mitigation: Review file paths before execution and only pass files that are intended for hosted processing.

Risk: Generic speech-related requests could accidentally trigger a hosted TTS call.

Mitigation: Invoke this skill explicitly and review the generated command before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses that may include hosted result URLs or saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, dLazy authentication, and network access to dLazy API and file endpoints.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
