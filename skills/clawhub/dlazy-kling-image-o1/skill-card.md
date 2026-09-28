## Description:

Helps agents generate and edit images with Kling Image O1 from text prompts and reference images through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating images from prompts or editing images with references using Kling Image O1.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images may be sent to dLazy's hosted service.

Mitigation: Confirm before submitting sensitive prompts or private images.

Risk: Logging in may save an API key locally.

Mitigation: Review local credential storage and avoid logging in on shared devices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Text guidance and CLI commands; CLI returns JSON with image URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be saved locally with the CLI.]

## Skill Version(s):

1.3.21 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
