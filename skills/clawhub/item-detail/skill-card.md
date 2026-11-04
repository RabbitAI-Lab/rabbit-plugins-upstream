## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to turn a product photo and verified selling points into modular Chinese-language product detail graphics for online listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompt text are sent to the chosen cloud provider for image generation.

Mitigation: Choose the provider explicitly, preview inputs with --dry-run, and use only assets approved for that provider. Provider retention practices were not independently verified.

Risk: Bundled cost estimates may disagree.

Mitigation: Confirm the selected provider's current pricing before generating images.

## Reference(s):

- [Model flags reference](artifact/references/model-flags.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [Generated image files for product detail graphics]

**Output Parameters:** [2D]

**Other Properties Related to Output:** [Modular ecommerce layouts with Chinese text; review generated text and product claims before publishing.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
