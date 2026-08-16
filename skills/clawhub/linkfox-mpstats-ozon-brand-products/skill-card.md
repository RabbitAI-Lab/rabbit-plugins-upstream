## Description:

MPSTATS Ozon 俄罗斯站按品牌下钻商品列表，按 Ozon 品牌展示名返回该品牌下商品的销量、销售额、价格、评分、库存、周转、损失销售额等指标，并支持数值筛选、排序和货币换算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace analysts and e-commerce operators use this skill to inspect all Ozon Russia products under a specific brand and compare SKU-level sales, revenue, price, stock, rating, and lost-sales metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends analytics requests and may handle account, API-key, phone/SMS login, and billing-order data during onboarding.

Mitigation: Install and run it only when that LinkFox data sharing is acceptable, and review authentication and billing flows before use.

Risk: Endpoint environment variables can redirect requests if overridden.

Mitigation: Verify LINKFOX_* endpoint environment variables point to trusted LinkFox hosts before running the scripts.

Risk: Saved API response files may contain marketplace analysis data that could be committed accidentally.

Mitigation: Run the skill in an appropriate workspace and exclude generated linkfox response directories from commits when needed.

Risk: Automatic feedback reporting can share task context or skill behavior observations.

Mitigation: Review or disable feedback reporting behavior if the deployment should minimize outbound data sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-brand-products)
- [MPSTATS Ozon brand products API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and optional saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may save complete API responses under a workspace linkfox data directory and print either full JSON or a compact summary depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
