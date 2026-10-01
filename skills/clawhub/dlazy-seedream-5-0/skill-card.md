## Description:

Generates 2K, 3K, or 4K images from prompts and optional reference images for posters, key visuals, and print designs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and design teams use this skill to generate high-resolution images from text or reference images for posters, key visuals, and print work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images are sent to dLazy services.

Mitigation: Send only content approved for third-party processing and review the service before use.

Risk: Authentication may store an API key locally.

Mitigation: Protect the local configuration or use the DLAZY_API_KEY environment-variable option.

Risk: Installing the third-party CLI requires trusting its package publisher.

Mitigation: Confirm trust in dLazy and the @dlazy/cli package before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Images]

**Output Format:** [JSON with generated image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K resolution, optional reference images, and asynchronous task IDs.]

## Skill Version(s):

1.2.19 (source: ClawHub release metadata; bundled skill text lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
