## Description:

Synthesize text into natural speech with Doubao TTS through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to generate Chinese or English speech from text, choose voice and speed options, and save or poll generated outputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends text prompts and generation parameters to dLazy's hosted API.

Mitigation: Avoid submitting sensitive text unless approved for the dLazy service, and review account controls and service terms before production use.

Risk: The skill depends on a pinned third-party npm CLI and stores an API key in local configuration or environment variables.

Mitigation: Review the pinned CLI package before installing, protect local credentials, and rotate or revoke dLazy API keys when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files]

**Output Format:** [CLI commands and JSON responses with generated asset URLs or saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports asynchronous task IDs, polling, and local saving through CLI options.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
