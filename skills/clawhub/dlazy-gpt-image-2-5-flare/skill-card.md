## Description:

Helps agents create and edit images from text prompts and optional reference images through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images with prompts, optional reference images, and selectable aspect ratio and quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference files are sent to the dLazy hosted service.

Mitigation: Avoid sensitive prompts and local files; review the service terms before use.

Risk: Using the CLI requires an installed or on-demand package and may store an API key locally after login.

Mitigation: Review the CLI before installation, use the pinned npx command if a global install is unwanted, and safeguard or rotate the API key as needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Image URLs]

**Output Format:** [CLI JSON result with generated image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to five reference images, selectable aspect ratio and quality, and asynchronous generation.]

## Skill Version(s):

1.2.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
