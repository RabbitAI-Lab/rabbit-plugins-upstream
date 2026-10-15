## Description:

Generate coherent transition videos from a first and last frame using Jimeng's video model through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request a transition video between supplied first and last frame images, with an optional prompt and duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied frame images can be sent to dLazy's third-party cloud service.

Mitigation: Confirm the user is comfortable sharing the content with dLazy; avoid sending sensitive prompts or media without permission.

Risk: Signing in can store a dLazy API key locally.

Mitigation: Use DLAZY_API_KEY for a per-invocation key when local credential storage is not desired.

Risk: Installing the third-party CLI globally persists software on the device.

Mitigation: Prefer the pinned npx invocation when a persistent global install is not desired.

Risk: Generic transition-video requests may activate the skill without a clear intent to use dLazy.

Mitigation: Confirm the intended service before running the CLI.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with generated asset URLs or an asynchronous task ID; results may optionally be saved locally.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
