## Description:

Generate images with Kling O1 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate or edit images with Kling O1 by providing a text prompt and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports that the shell behavior starts dLazy authentication, which differs from the stated image-generation purpose; some related references could not be resolved.

Mitigation: Review the install and service details before use, and understand how authentication, prompts, and supplied media are handled.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Image URLs, JSON]

**Output Format:** [JSON result envelope with generated image URLs; image files can also be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous mode may return a task ID before image generation finishes.]

## Skill Version(s):

1.3.39 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
