## Description:

生成带中文排版的详情页模块。商品图 + 卖点 → 可直接上架的详情页图文模块。当用户说「详情页」「做详情图」「商品描述图」「详情页模块」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and ecommerce content creators use the skill to turn a product photo and supplied selling points into Chinese-labeled product-detail image modules, such as banners, benefit rows, material and detail panels, and size charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends product images and prompts to an external image-generation provider; the security assessment advises caution with sensitive information.

Mitigation: Review the selected provider's data handling and avoid sending product images or prompts that contain information you are not comfortable sharing.

Risk: The security assessment is suspicious and incomplete: only 5 of 9 components were fully inspected, with some analyses degraded.

Mitigation: Consider these scan limitations and concerns when deciding whether to install or use the skill.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Model flags](references/model-flags.md)
- [Provider CLI and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [Product-detail image files, typically JPEG]

**Output Parameters:** [Image modules in 3:4, 1:1, or 9:16 ratios; 2K recommended]

**Other Properties Related to Output:** [Chinese text layout; modules can include banners, selling points, material and detail panels, and size charts.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
