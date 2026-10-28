## Description:

Generate/edit images with Nano Banana Pro. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts or edit images they provide through Nano Banana Pro.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy services for generation.

Mitigation: Send only prompts and images that are appropriate to share with the service.

Risk: Login stores an organization API key in the local CLI configuration, and generation uses paid credits.

Mitigation: Use the DLAZY_API_KEY environment variable if you prefer not to save the key locally, and use --dry-run to inspect the estimated cost before generation.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [Image files or hosted image URLs, with JSON result or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image with up to 14 reference images; includes aspect-ratio, image-size, and asynchronous task options.]

## Skill Version(s):

1.2.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
