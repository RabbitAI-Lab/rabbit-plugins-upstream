## Description:

商品图生成带文案排版的转化主图。商品图 + 卖点 → 带中文文案的电商主图。当用户说「主图」「加卖点文案」「转化图」「促销图」「主图文案」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and marketing teams use this skill to turn product images and selling-point copy into promotional product-main images with Chinese text layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied product images are sent to a cloud generation provider.

Mitigation: Choose an approved provider explicitly and preview routing with --dry-run before sending confidential product or campaign details; check the provider's retention policy.

Risk: Batch generation and automatic retries can increase generation charges.

Mitigation: Review estimated costs and batch settings before submitting requests.

Risk: Generated files may overwrite or mix with existing assets if paths are reused.

Mitigation: Use a dedicated output path and a reviewed CLI version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI guidance](artifact/references/provider-cli.md)
- [Model parameters](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [Generated product-marketing image files, with accompanying prompt and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images may be generated in batches and saved to a user-selected path.]

## Skill Version(s):

1.0.25 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
