## Description:

Generate high-quality images with Vidu Q2 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can generate images from text prompts or use reference images for image-to-image generation with Vidu Q2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy's hosted service, and local image files may be uploaded for processing.

Mitigation: Upload only prompts and images you are comfortable sharing with dLazy.

Risk: Image generation uses service credits, and login stores an organization API key in the local CLI configuration.

Mitigation: Choose Vidu Q2 deliberately, expect credit charges, and use the DLAZY_API_KEY environment variable if you want to avoid persistent local key storage.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (listed in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with a JSON response containing hosted image URLs and output metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task status; generated images can optionally be saved to a local path.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
