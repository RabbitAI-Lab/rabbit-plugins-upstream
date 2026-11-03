## Description:

Image generation skill. Automatically selects the best dlazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can request image generation or image editing, then use the returned media URLs in their workflows. The skill selects a suitable dLazy image tool from the prompt and can also upscale, remove backgrounds, or vectorize images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services, and generation can incur charges.

Mitigation: Use the service only when appropriate, limit video or speech generation to requests that need it, and review dLazy's terms and charges before sending prompts or media.

Risk: The CLI stores an API key locally, and the skill's review does not audit the external package.

Mitigation: Protect the stored API key and review the pinned CLI before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, SVG files, Media URLs, JSON]

**Output Format:** [Hosted media URLs in a JSON CLI envelope; generated raster images and SVG media are available from dLazy URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The selected tool may generate or edit images, upscale or matte images, or convert raster images to SVG.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
