## Description:

MPSTATS Ozon 俄罗斯站商品搜索与反查，按俄语关键词或 SKU 在 MPSTATS 数据库中检索 Ozon 商品，返回商品 ID、标题、品牌和卖家信息，是 Ozon 选品与竞品链路的起点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, ecommerce analysts, and agents use this skill to search or reverse-lookup Ozon Russia products by Russian keyword or SKU before moving into product detail, brand, category, or seller drill-down workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox and MPSTATS network services and may consume paid credits.

Mitigation: Confirm the intended search parameters and credit impact before running searches, retries, recharge flows, or payment-order commands.

Risk: Account setup paths can collect phone and SMS verification details and help persist an API key.

Mitigation: Prefer self-service API-key setup, avoid shared machines for shell-profile secrets, and restart sessions after changing environment variables.

Risk: Environment variables can alter LinkFox service endpoints.

Mitigation: Review LINKFOX_* URL environment variables before use and keep them pointed at expected LinkFox services.

Risk: Full search responses are written to local linkfox folders.

Mitigation: Run the skill from an appropriate workspace and review saved result files before sharing or committing them.

## Reference(s):

- [MPSTATS Ozon 商品搜索 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-search)
- [LinkFox skill catalog](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses or saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results contain Ozon product identity fields only; full API responses are persisted under a local linkfox directory and larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
