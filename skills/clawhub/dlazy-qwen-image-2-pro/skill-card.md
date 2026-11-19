## Description:

Alibaba Bailian qwen-image-2.0-pro general image generation, with strong text rendering, multi-line layout, photorealistic detail, and semantic adherence for mixed text and image designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can use this skill to generate images from text prompts, optionally using reference images, for designs that need detailed scenes or rendered text. It returns generated image results through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment notes a CLI login operation and incomplete evidence for this image-generation skill.

Mitigation: Review the CLI and its login flow before authenticating.

Risk: Prompts and any supplied local images are sent to dLazy for generation, and generated image URLs are hosted by the service.

Mitigation: Avoid sending sensitive prompts or media unless you are comfortable with dLazy processing them.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON results with generated image URLs; optionally downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation; --save downloads the generated image locally.]

## Skill Version(s):

1.3.42 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
