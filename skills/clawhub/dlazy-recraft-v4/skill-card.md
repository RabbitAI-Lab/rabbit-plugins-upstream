## Description:

Helps agents generate 1MP raster images with Recraft V4 for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and developers use this skill to generate raster images for creative projects and fast design iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be sent to dLazy, and generated images are hosted by the service.

Mitigation: Avoid submitting sensitive prompts or files unless the service's handling of that data is acceptable.

Risk: Authentication may save an API key in local user configuration.

Mitigation: Protect the user configuration and rotate or revoke the key through the dLazy dashboard if needed.

Risk: Installing the CLI globally leaves a persistent executable on the system.

Mitigation: Use the pinned on-demand npx invocation when a persistent global installation is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image-generation service returns hosted image URLs; results can also be saved locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
