## Description:

商品图生成带文案排版的转化主图。商品图 + 卖点 → 带中文文案的电商主图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce teams use this skill to turn a product photo and verified selling points into a promotional main image with Chinese text layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags possible transmission of product images and prompts to an external image-generation provider and notes that inspection was incomplete; it does not establish that the calls are malicious.

Mitigation: Before use, identify the provider that will receive the images and prompts, review its data-handling terms, and avoid sending material you cannot share.

## Reference(s):

- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)
- [Related item detail skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/item-detail/skill.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Guidance, Shell commands]

**Output Format:** [Raster ecommerce main image, typically square, with generated Chinese selling-point text; accompanied by prompt and command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one product image and optional layout reference; the documented default is square 2K output with a batch of three candidates.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
