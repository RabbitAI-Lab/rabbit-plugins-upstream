## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate Chinese or English speech from text through the dLazy CLI and hosted Doubao TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and generation parameters are sent to dLazy's hosted API for inference.

Mitigation: Review prompts for sensitive content before use and follow the service terms for hosted processing.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation environment variables or npx when persistent local credentials or global CLI installation are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated audio asset URLs or saved files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
