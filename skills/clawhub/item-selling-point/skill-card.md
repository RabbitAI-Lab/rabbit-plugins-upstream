## Description:

Creates Chinese-language e-commerce product images with selling-point copy, layout, and optional promotional badges from a product photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use a product photo and verified selling points to make readable Chinese-language main listing images, including optional promotional copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and marketing copy are sent to dLazy or the configured image provider.

Mitigation: Use approved providers and appropriate API keys; confirm permission to share product assets before generation.

Risk: Generated copy or imagery may misstate product features or promotions, or be illegible at listing size.

Mitigation: Verify claims and discounts against product information, check product fidelity and Chinese text, and inspect a thumbnail before publishing.

Risk: Cloud generation may incur charges or save files outside the intended location.

Mitigation: Check a dry run first and select an intended workspace output path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI and data-flow reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated JPG product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 1:1 or 3:4 layouts and optional promotional badges.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
