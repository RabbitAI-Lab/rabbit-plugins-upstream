## Description:

Generate and edit images with Nano Banana Pro using text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from prompts or edit images with Nano Banana Pro through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a login-command mismatch and incomplete scan coverage because referenced paths, including the CLI package, were unavailable.

Mitigation: Review the CLI package and its login behavior before installing, and proceed only if the command's purpose is clear to you.

Risk: Prompts and local reference images are sent to dLazy's hosted API and media storage for image generation.

Mitigation: Avoid sending sensitive or confidential prompts and images unless your organization's policies permit using the hosted service.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata (server provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image assets, JSON result metadata]

**Output Format:** [Generated images as hosted URLs or saved image files, with JSON status and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and up to 14 reference images; supports aspect ratio, image size, and asynchronous generation options.]

## Skill Version(s):

1.2.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
