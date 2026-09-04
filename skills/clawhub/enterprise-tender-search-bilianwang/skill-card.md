## Description:

Helps agents search Chinese tender, procurement, award, company, supplier, competitor, and market data through the 必联网 and 知了标讯 API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, sales teams, and business development analysts use this skill to find tender opportunities, verify suppliers and buyers, inspect company bidding histories, and summarize market demand. It can also help agents answer account balance and usage questions for the configured API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives procurement, company, supplier, competitor, and market-analysis queries sent through the integration.

Mitigation: Use the skill only for queries that are appropriate to share with the provider, and avoid sending confidential procurement strategy or restricted company information unless approved.

Risk: If no API key is configured, the opt-in trial flow hashes a MAC address, creates or reuses a trial account, and stores an API key under ~/.zlbx/config.json.

Mitigation: Prefer setting ZLBX_API_KEY directly for managed deployments, and require explicit user consent before any automatic registration or local key storage occurs.

Risk: When quota runs out, the auto-registered flow may generate an auto-login recharge link.

Mitigation: Treat generated recharge links as account-access links, show them only to the intended user, and use the manual account portal for user-provided API keys.

## Reference(s):

- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)
- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-tender-search-bilianwang)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with tables, links, JSON request examples, and concise configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY environment variable or an approved local trial-account registration flow.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
