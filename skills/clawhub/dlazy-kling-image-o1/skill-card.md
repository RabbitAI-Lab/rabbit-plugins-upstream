## Description:

Generates images from text prompts or reference images using Kling Image O1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text or adapt supplied reference images with Kling Image O1 via dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images may be sent to dLazy for generation.

Mitigation: Send only content you are comfortable sharing with dLazy.

Risk: CLI login saves an API key locally.

Mitigation: Use a per-invocation DLAZY_API_KEY if you do not want a saved CLI key.

Risk: Global installation runs a third-party npm package.

Mitigation: Review the pinned dLazy CLI package before installing it globally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result containing generated-image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and reference-image generation; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
