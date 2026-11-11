## Description:

Generate high-quality images from text prompts or reference images using Doubao Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can generate images from text prompts or use reference images to guide image-to-image generation. The skill sends requests through dLazy's hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is partial and says several local path-like references could not be resolved.

Mitigation: Review the CLI and any unresolved references before installing or running the skill.

Risk: The security assessment reports a possible mismatch between the image-generation purpose and a CLI login action.

Mitigation: Review the CLI login flow before authenticating or proceeding with installation.

Risk: Prompts and supplied reference images are sent to dLazy's hosted service, and local image files are uploaded for processing.

Mitigation: Avoid submitting confidential prompts or images unless the service's data handling is acceptable for them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON result with generated image URLs and metadata; an image file can also be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation accepts a text prompt and optional reference images, resolution, and aspect ratio. Image requests use dLazy's hosted service.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
