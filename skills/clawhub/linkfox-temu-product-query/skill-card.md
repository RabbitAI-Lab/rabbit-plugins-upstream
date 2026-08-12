## Description:

按多维度筛选 Temu 商品，包括关键词、商品 ID、店铺 ID、类目、价格、评分、评论、销量、上架时间、托管模式、地区和标签等。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and filter Temu product data for product research, ecommerce selection, and competitive analysis. It can also guide users through LinkFox API key setup or billing recovery when authentication or balance errors occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts LinkFox services and can use LINKFOX_* environment overrides for service URLs.

Mitigation: Install only when LinkFox service access is expected, and run with trusted LINKFOX_* environment values.

Risk: The onboarding flow can handle phone verification codes, API keys, billing plans, and payment ordering.

Mitigation: Review onboarding and billing steps before use, and treat verification codes, generated API keys, payment links, and order details as sensitive.

Risk: The query script stores full product lookup responses in a local linkfox session directory.

Mitigation: Review stored response files for sensitive business data and apply local retention or cleanup controls appropriate for the workspace.

## Reference(s):

- [Temu 商品查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-product-query)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May store full API responses under a local linkfox session directory and summarize larger responses inline.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
