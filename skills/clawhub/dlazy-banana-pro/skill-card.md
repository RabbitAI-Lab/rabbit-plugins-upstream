## Description:

Generate/edit images with Nano Banana Pro. Supports text-to-image and image-to-image. 使用 Nano Banana Pro 生成/编辑图片，支持文生图与图生图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent to create images from text prompts or edit images with optional reference images through dLazy's hosted Nano Banana Pro service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy's hosted service; local image files may be uploaded to its media storage.

Mitigation: Use the skill only when comfortable sharing the prompts and selected images with dLazy.

Risk: The dLazy API key is stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Keep the API key private and rotate or revoke it through the documented dLazy dashboard if needed.

Risk: Using the hosted image generation service can spend dLazy service credits.

Mitigation: Review the CLI's dry-run cost estimate before making a request when cost is a concern.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files or hosted image URLs with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image generation; aspect ratio and image size are configurable.]

## Skill Version(s):

1.2.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
