## Description:

Generates 2K, 3K, or 4K images from prompts and reference images for key visuals, posters, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate high-resolution images from text prompts, with optional reference images, for visual design and print materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes an install-related concern and incomplete scan evidence.

Mitigation: Review the pinned CLI package and installation steps before installing; use the documented npx option to avoid a global install.

Risk: The CLI requires a dLazy API key and stores it in user configuration unless supplied through the environment.

Mitigation: Keep the key private and rotate or revoke it through the dLazy dashboard if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI project page (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON result data]

**Output Format:** [Generated image URLs in a JSON result; optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [2K, 3K, or 4K resolution; selectable aspect ratio; up to 10 reference images; synchronous or asynchronous result handling.]

## Skill Version(s):

1.2.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
