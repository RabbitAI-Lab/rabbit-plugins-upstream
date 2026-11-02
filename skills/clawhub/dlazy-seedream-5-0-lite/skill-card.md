## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other image creators use this skill to generate images from text prompts or refine results with reference images through dLazy's Seedream 5.0 Lite service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are uploaded to dLazy for generation.

Mitigation: Send only prompts and images that are appropriate to share with the service.

Risk: Image generation can consume paid credits.

Mitigation: Review the cost estimate with the CLI's dry-run option before generating.

Risk: Logging in saves a dLazy API key in the local CLI configuration.

Mitigation: Use a trusted account and device, and rotate or revoke the key if needed; review the third-party CLI before installing it.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON result metadata]

**Output Format:** [Generated image assets with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a text prompt and optional reference images; resolution, aspect ratio, and asynchronous completion can be configured.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
