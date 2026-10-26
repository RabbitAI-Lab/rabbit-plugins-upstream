## Description:

Generate high-quality images with Vidu Q2. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate images from text prompts or create image variations from reference images with Vidu Q2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media are sent to dLazy cloud services for image generation.

Mitigation: Submit only prompts and images appropriate for cloud processing.

Risk: Image generation may incur organization costs.

Mitigation: Review the cost estimate and available credits before running a generation.

Risk: The CLI stores the organization API key in local configuration.

Mitigation: Restrict access to the key and its configuration file; rotate or revoke the key if exposed.

Risk: The skill uses a pinned third-party CLI package.

Mitigation: Review the pinned CLI release before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [JSON response with generated image URLs and task status; optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image results are hosted URLs; asynchronous requests may initially return a task ID.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
