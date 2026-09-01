## Description:

商品图生成带文案排版的转化主图。商品图 + 卖点 → 带中文文案的电商主图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent users use this skill to turn a product image plus selling points into a square Chinese ecommerce main-image prompt and generation command. It supports product-image composition with concise feature copy, promotional badges, category-based styling, and output review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to dLazy or another configured image provider.

Mitigation: Use only approved product assets and credentials, and confirm the selected provider's data-handling posture before generation.

Risk: Generated marketing copy or promotional badges may make inaccurate or noncompliant claims.

Mitigation: Review generated claims and promotions for accuracy, avoid absolute claims, and use only verified offers before publication.

Risk: Generated Chinese text may be unreadable, malformed, or too small at marketplace thumbnail size.

Mitigation: Keep copy short, generate multiple candidates, and inspect the selected output at about 200 by 200 pixels before use.

Risk: Image generation may alter the product's shape, color, material, or logo.

Mitigation: Include product-fidelity constraints in the prompt and compare the output against the source product image before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy product site](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically uses one product image, optional layout reference image, square or vertical main-image size settings, and batch generation for selecting legible Chinese typography.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
