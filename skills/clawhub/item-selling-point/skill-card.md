## Description:

根据商品图片和卖点文案生成带中文排版的电商主图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营和设计人员使用商品图片、功能卖点与真实促销信息制作适合商品列表展示的方形中文主图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts and selected brand assets may be sent to an external image provider.

Mitigation: Use a dry run to check the provider and credentials; do not submit confidential images without confirming the provider's data policy.

Risk: Batch image generation may incur provider charges.

Mitigation: Confirm estimated costs before generating batches.

Risk: Generated text or imagery may misstate product features, promotions or appearance.

Mitigation: Verify claims and discounts against product details and inspect the final image at thumbnail size before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Square ecommerce image files with optional Markdown guidance and JSON execution status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese selling-point copy and promotional badge; local output file for review.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
