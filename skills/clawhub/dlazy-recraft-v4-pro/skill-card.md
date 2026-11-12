## Description:

4MP high-resolution raster image generation. Suitable for print-ready assets and large-scale use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate high-resolution raster images from prompts for print-ready and large-format assets, with optional aspect-ratio selection and local saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found authentication setup that was not clearly connected to the image-generation purpose, with partial scanner coverage.

Mitigation: Review the CLI and confirm you trust dLazy before configuring an API key; use the documented rotation or revocation controls if needed.

Risk: Prompts and any local media provided to the skill are sent to dLazy's hosted service for generation.

Mitigation: Review prompts and input media before sending, and avoid including content you do not want processed by the hosted service.

## Reference(s):

- [dLazy CLI homepage (listed in release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)

## Skill Output:

**Output Type(s):** [Images, Files]

**Output Format:** [High-resolution raster image (PNG), returned as a hosted URL or saved to a local path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports selectable aspect ratios; asynchronous jobs may return a task identifier before the image is ready.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
