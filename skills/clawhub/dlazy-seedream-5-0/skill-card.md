## Description:

Generates high-resolution Doubao Seedream 5.0 images from text prompts and reference images, for key visuals, posters, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate 2K, 3K, or 4K Seedream images for key visuals, posters, and print, using a text prompt and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was benign with medium confidence, but the partial scan could not resolve the pinned CLI package and flagged a mismatch between the skill's image-generation purpose and observed login behavior.

Mitigation: Before installing, review the pinned @dlazy/cli package and confirm that its device-code login and local API-key storage behavior are acceptable.

Risk: Prompts and local reference images are sent to dLazy-hosted services for generation.

Mitigation: Avoid submitting prompts or images that contain information you do not want sent to the hosted service.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image files (PNG) and JSON result metadata with hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K resolution, multiple aspect ratios, and up to 10 reference images; asynchronous task status is available when requested.]

## Skill Version(s):

1.2.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
