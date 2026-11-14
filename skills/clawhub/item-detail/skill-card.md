## Description:

Generates Chinese-language product detail page image modules from product photos and supplied selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to turn product photos and verified selling points into modular detail-page visuals, including banners, feature blocks, material panels, and size charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and supplied text may be sent to external image-generation providers.

Mitigation: Before generation, confirm you are authorized to share the inputs and review what the selected provider receives and how it handles the data.

Risk: Generated Chinese text may be garbled or introduce inaccurate product claims, and the product's appearance may change.

Mitigation: Use only verified selling points, inspect every generated text and image for accuracy, and correct errors before publishing.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [Watermark removal recommendation](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/remove-watermark/skill.md)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-detail)

## Skill Output:

**Output Type(s):** [Images, Prompt text, Shell commands]

**Output Format:** [Product detail image files (JPEG, PNG, or WebP), with prompts and optional command examples in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated in separate page modules with configurable image inputs, layout prompts, aspect ratios, resolution, and batch count.]

## Skill Version(s):

1.0.32 (source: frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
