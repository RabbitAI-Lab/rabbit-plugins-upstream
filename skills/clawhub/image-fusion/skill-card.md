## Description:

Helps create a cohesive e-commerce outfit image from up to eight product photos, with optional pose and model references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants, designers, and content teams use this skill to plan and generate coordinated product-outfit images for e-commerce catalogs from separate garment and accessory photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or model photos, prompts, and image URLs are sent to the configured generation provider.

Mitigation: Check the selected provider with dry-run before generating and avoid sensitive or unlicensed images.

Risk: Example model demographics and brand defaults may not fit the intended catalog.

Mitigation: Edit the example demographics and brand settings before use.

## Reference(s):

- [ClawHub image-fusion release](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider and CLI guide](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown instructions and prompts with shell commands; generated images may be saved as files by the selected provider.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to eight product images, optional model and scene references, and dry-run checks before generation.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
