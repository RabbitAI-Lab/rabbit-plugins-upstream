## Description:

Generate high-quality images with Doubao Seedream 4.5 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can create images from text prompts or use reference images to guide image generation. The skill sends requests to dLazy's hosted service and returns generated image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted that the CLI login behavior is not clearly connected to the advertised image-generation purpose.

Mitigation: Review the CLI package, installation details, and authentication flow before installing or signing in.

Risk: Some security reference checks were unresolved, leaving the review evidence incomplete.

Mitigation: Review the skill and its install details before use.

Risk: Reference images provided from local paths are uploaded to dLazy media storage for generation.

Mitigation: Only submit images that are appropriate to share with the hosted service.

## Reference(s):

- [CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with a JSON result containing image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image resolution and aspect ratio are configurable; image-to-image generation accepts reference images.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
