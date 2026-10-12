## Description:

Helps agents generate images from text prompts or reference images using Doubao Seedream 5.0 Lite through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to request text-to-image or image-to-image generation with configurable size and resolution, then retrieve the resulting image URL or saved file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images may be sent to the third-party dLazy service.

Mitigation: Avoid sending sensitive prompts or private images unless uploading them to dLazy is acceptable.

Risk: Image generation may consume paid credits.

Mitigation: Check the cost estimate with the dry-run option before submitting requests.

Risk: Login can store an API key in the local CLI configuration.

Mitigation: Use per-invocation environment-variable authentication if local key persistence is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing image URLs; an optional flag saves the image locally.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; skill file frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
