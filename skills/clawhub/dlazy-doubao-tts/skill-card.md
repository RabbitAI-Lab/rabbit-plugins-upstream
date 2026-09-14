## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to synthesize prompt text into Chinese or English speech through the dLazy CLI and hosted Doubao TTS API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local inputs are sent to dLazy cloud endpoints for inference.

Mitigation: Avoid submitting sensitive content unless the user accepts dLazy processing, and avoid passing local file paths unless upload is intended.

Risk: The skill relies on an external npm CLI and hosted API.

Mitigation: Use the pinned CLI version, review the linked source before installation, and prefer per-invocation or sandboxed use when possible.

Risk: The CLI can save generated assets to local paths.

Mitigation: Confirm any --save destination before writing files.

Risk: A dLazy API key is required and may be stored in local configuration or supplied through an environment variable.

Mitigation: Store keys outside project files, rotate or revoke keys from the dLazy dashboard when needed, and do not commit credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Audio]

**Output Format:** [JSON response with generated audio URLs, async task identifiers, or saved audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; can run synchronously or return a generateId for later polling.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
