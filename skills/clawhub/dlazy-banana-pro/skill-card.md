## Description:

Generate and edit images with Nano Banana Pro from text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can generate images from prompts or edit images using reference images. The skill sends prompts and any supplied images to dLazy's hosted service and can return image URLs or save generated images locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images are sent to dLazy, and local image files are uploaded to its media storage; generation may incur charges.

Mitigation: Submit only prompts and images you are comfortable uploading, and use the dry-run option to review the cost estimate before generation.

Risk: The login flow saves a reusable API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable when you prefer not to save a key through login; rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON, Text]

**Output Format:** [Generated image URLs in a JSON response, with optional image files saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation or editing; image size and aspect ratio are configurable.]

## Skill Version(s):

1.2.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
