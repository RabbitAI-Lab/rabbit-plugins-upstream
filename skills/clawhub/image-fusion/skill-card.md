## Description:

Creates coordinated ecommerce model photos from up to eight individual product images, with guidance for preserving each item's appearance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and sellers use this skill to combine clothing and accessory product photos into consistent full-look images for storefronts and product pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or model images and prompts are sent to the selected image provider.

Mitigation: Use an approved provider and avoid submitting sensitive images or files without permission.

Risk: Image generation may incur charges or produce inaccurate garment details.

Mitigation: Check the selected provider credentials, estimate costs with --dry-run, and review generated images before publishing.

Risk: The default model description may not suit the intended audience.

Mitigation: Adjust the model description in the prompt to match the desired representation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and shell commands; generated ecommerce images saved as files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to eight product images per look; optional pose and model references; provider-dependent batch and image resolution.]

## Skill Version(s):

1.0.23 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
