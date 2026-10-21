## Description:

Helps agents generate short videos with MiniMax Hailuo from text, first and last frames, or reference media through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short generated videos from text prompts, frame transitions, or image, video, and audio references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to the third-party dLazy cloud service.

Mitigation: Avoid supplying private or sensitive prompts and media unless the service's handling is acceptable.

Risk: Signing in may store a dLazy API key on the user's device.

Mitigation: Protect local account access and rotate or revoke the key if it is exposed.

Risk: Installing the third-party CLI globally persists an executable on the device.

Mitigation: Review the CLI before installation and use the documented npx option if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples and descriptions of generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service can return hosted video links or asynchronous task identifiers; generated media may be downloaded locally.]

## Skill Version(s):

1.2.29 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
