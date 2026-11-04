## Description:

商品图生成带文案排版的转化主图。商品图 + 卖点 → 带中文文案的电商主图。当用户说「主图」「加卖点文案」「转化图」「促销图」「主图文案」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce marketers use this skill to turn a product photo and verified selling points into a Chinese-language promotional listing image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and copy are sent to the selected cloud provider; the artifacts do not establish that provider's retention practices.

Mitigation: Choose the provider explicitly and submit only images and copy approved for that provider.

Risk: Batch generation and retries can incur charges.

Mitigation: Use --dry-run to check the destination, inputs, and estimated cost, and set batch size deliberately.

## Reference(s):

- [Provider and CLI guide](references/provider-cli.md)
- [Seedream model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files]

**Output Format:** [Generated image file, typically JPEG at 1:1 (2K)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A product image with Chinese selling point copy; optional layout reference image; batch runs can produce multiple variants.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
