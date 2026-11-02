## Description:

Generate high-quality images with Doubao Seedream 4.5. Supports text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate images from text prompts or transform images using Doubao Seedream 4.5 through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy's hosted service; login saves an API key locally; generation may consume credits.

Mitigation: Only submit prompts and images you are comfortable sharing, protect or rotate the saved API key, and use --dry-run to preview the request and estimated cost.

## Reference(s):

- [CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Files]

**Output Format:** [Generated image assets, with result metadata and hosted URLs in JSON]

**Output Parameters:** [2D; configurable aspect ratio and 2K or 4K resolution]

**Other Properties Related to Output:** [Prompt-guided; accepts up to 10 reference images and supports asynchronous generation.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
