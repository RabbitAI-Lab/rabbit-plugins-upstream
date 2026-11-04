## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to create images from text prompts or generate variations guided by reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy's hosted service, and generation can consume credits.

Mitigation: Use the skill for explicit image-generation requests, preview the request and estimated cost with --dry-run, and avoid sending sensitive prompts or images.

Risk: The CLI stores the API key in its local configuration when authenticated.

Mitigation: Protect the saved API key and rotate or revoke it if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI repository (CLI reference)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON response]

**Output Format:** [Generated image files with a JSON response containing result details and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image generation; resolution and aspect ratio can be selected.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
