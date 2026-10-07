## Description:

Generates images from text prompts or reference images using Kling Image O1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or reference images through the dLazy-hosted Kling Image O1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images may be sent to dLazy's hosted service.

Mitigation: Share only content you are comfortable uploading to dLazy.

Risk: Image generation may consume account credits.

Mitigation: Check the cost estimate with dry-run before submitting a request.

Risk: The CLI may store an API key locally.

Mitigation: Use a per-invocation API key environment variable if local key storage is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved locally on request.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
