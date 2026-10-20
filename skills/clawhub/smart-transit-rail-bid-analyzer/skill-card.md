## Description:

帮助用户检索智慧交通与轨道交通招投标信息，并分析基建项目、企业、品牌、价格和市场商机。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

采购、销售及市场分析人员可检索交通基建招投标与拟建项目，识别潜在客户和竞争对手，并分析采购趋势、中标品牌及历史价格。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts 知了标讯 services using an API key and may save a newly issued key on the local device.

Mitigation: Review the service and credential-storage behavior before use; set ZLBX_API_KEY manually to avoid automatic local credential creation.

Risk: Trial registration sends platform and architecture details plus a hashed MAC-derived device identifier for de-duplication.

Mitigation: Require informed user consent before registration; use manual registration if device-data collection is not acceptable.

Risk: Account and update checks, referral links and quota-related login prompts may be unsuitable for sensitive environments.

Mitigation: Review these interactions and links before installation; do not use the skill where such calls or promotions violate policy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/smart-transit-rail-bid-analyzer)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)
- [招投标搜索接口说明](artifact/references/api-search.md)
- [企业分析接口说明](artifact/references/api-company.md)
- [市场分析接口说明](artifact/references/api-market.md)
- [自动注册与隐私说明](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries, linked result tables and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the provider's data and available account credits.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
