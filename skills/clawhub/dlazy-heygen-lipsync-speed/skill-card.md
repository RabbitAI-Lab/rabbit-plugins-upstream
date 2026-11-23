## Description:

Provides access to HeyGen Lipsync Speed, a fast lip-sync generation model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to submit video and audio inputs to the HeyGen Lipsync Speed service and retrieve generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The visible command is `dlazy login`, which does not clearly match the stated lip-sync generation purpose.

Mitigation: Review the CLI help and verify the command behavior with non-sensitive inputs before relying on the skill for generation.

Risk: Prompts and local media files may be sent to dLazy services, and generated media may be hosted remotely.

Mitigation: Only submit prompts and media that are appropriate to process through the service, and review its terms before use.

Risk: The CLI stores an API key in the user's local configuration unless an environment variable is used.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: The available scan was partial because some referenced paths could not be resolved.

Mitigation: Review the referenced CLI project and skill behavior before installation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video]

**Output Format:** [JSON result with generated media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media may be hosted remotely; asynchronous runs may initially return a task identifier.]

## Skill Version(s):

1.3.46 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
