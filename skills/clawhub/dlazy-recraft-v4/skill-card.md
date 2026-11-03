## Description:

1MP raster image generation with refined design judgment. Suitable for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can generate raster images from text prompts, choose an aspect ratio, and save generated assets for everyday creative work and rapid iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media are sent to dLazy's hosted service for generation.

Mitigation: Use the skill only when you trust dLazy with the prompts and media you provide.

Risk: The CLI stores an API key locally, and image generation consumes service credits.

Mitigation: Protect the stored key and rotate or revoke it as needed; check available credits before generation.

Risk: The external CLI package's runtime security claims were not independently verified.

Mitigation: Review the package and install only a version and source you trust.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [Raster image assets, returned as hosted URLs or saved files (the documented example is PNG)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Approximately 1MP; aspect ratio can be selected from supported presets or set to auto.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
