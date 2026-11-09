## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create images from text prompts or transform reference images with Doubao Seedream 5.0 Lite through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flagged a possible mismatch between image generation and login-only behavior.

Mitigation: Review whether the login flow matches the expected image-generation workflow before use.

Risk: The security scan flagged broad trigger wording and a whitespace finding for review.

Mitigation: Review the trigger wording and flagged text before enabling the skill.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs and metadata; optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts and up to 10 reference images; resolution and aspect ratio are configurable.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
