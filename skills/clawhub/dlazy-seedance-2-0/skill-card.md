## Description:

Helps agents generate video from text prompts, reference images, video, audio, or specified first and last frames through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text or media references and retrieve the resulting media link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service.

Mitigation: Only submit prompts and files you are comfortable sharing with the service.

Risk: Login may store an API key on the local device.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: A global CLI installation persists on the device.

Mitigation: Use the pinned npx invocation when a persistent installation is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and CLI JSON with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download or asynchronous task ID.]

## Skill Version(s):

1.3.29 (source: server-resolved release; skill frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
