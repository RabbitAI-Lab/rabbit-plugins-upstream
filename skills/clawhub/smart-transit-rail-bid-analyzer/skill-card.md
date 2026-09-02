## Description:

A Chinese-language procurement-data assistant for searching and analyzing smart-transit, rail, highway, ETC, signaling, and transportation-infrastructure bidding opportunities through the ZhiLiaoBiaoXun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business-development, procurement, market-analysis, and bidding teams use this skill to find transportation-infrastructure opportunities, inspect bid timelines, compare purchasers and suppliers, analyze competitors, and review price or market trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement searches and account-authenticated requests are sent to an external bidding-data service.

Mitigation: Use the skill only when that data sharing is acceptable, and configure ZLBX_API_KEY explicitly if account routing should be controlled.

Risk: Trial registration can derive a device identifier when no API key is configured.

Mitigation: Decline auto-registration or preconfigure ZLBX_API_KEY to avoid the device-derived trial-registration flow.

Risk: Stored API keys and auto-login recharge links can grant access to account or billing workflows.

Mitigation: Treat ~/.zlbx/config.json, API keys, and auto-login links as private credentials and avoid posting them in conversations or shared logs.

Risk: Company contact data may include masked or account-tiered contact information.

Mitigation: Display contact fields as returned, do not attempt to reconstruct masked phone numbers, and avoid bulk contact export.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-transit-rail-bid-analyzer)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown or text responses with structured tables, concise analysis, and inline API or shell examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated trial registration before account-authenticated data requests.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
