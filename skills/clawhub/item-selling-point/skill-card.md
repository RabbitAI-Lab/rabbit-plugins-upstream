## Description:

Guides an agent to turn product photos and verified selling points into e-commerce hero images with legible Chinese copy and promotional badges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to prepare product hero images with short Chinese selling points and verified promotional offers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the configured image-generation provider.

Mitigation: Check which provider credentials are configured, use trusted local files or HTTPS image URLs, and avoid private or sensitive photos.

Risk: Generated Chinese copy or promotional claims may be inaccurate or hard to read.

Mitigation: Review the generated image at thumbnail size and verify all product claims, prices, and promotions before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Image model parameters](references/model-flags.md)
- [Image provider and data-flow guidance](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands for generating JPEG or PNG product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically square product images with Chinese selling-point text and an optional promotion badge.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
