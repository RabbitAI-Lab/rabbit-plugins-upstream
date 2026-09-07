## Description:

招投标商机情报与竞对动态分析助手，用于查找临期或即将到期项目、挖掘续约商机、追踪竞对中标动态、分析采购单位与供应商，并监控行业或地区招标动态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, channel, and competitive-intelligence users use this skill to search tender and award data, identify expiring contracts and proposed projects, profile companies, and summarize market activity from the ZhiLiaoBiaoXun API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-registration may send a MAC-derived device identifier to the vendor.

Mitigation: Prefer a manually provisioned ZLBX_API_KEY, or decline auto-registration when device fingerprinting is not acceptable.

Risk: Generated auto-login or recharge links can function as temporary credentials.

Mitigation: Treat those links as sensitive, avoid sharing them, and regenerate only when needed.

Risk: Procurement search and company-contact workflows can surface project contact data.

Mitigation: Show contact data only as returned by the service, respect masked contact responses, and avoid bulk exporting contacts.

Risk: Vendor-controlled notices or referrals may be appended to responses.

Mitigation: Review generated responses before relying on or forwarding them in a business context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-opportunity-intelligence-officer)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto Registration Flow](references/auto-register.md)
- [ZhiLiaoBiaoXun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiaoBiaoXun Web API](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured API request or response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bid tables, company profiles, market summaries, account status, setup guidance, and temporary login or recharge links when supported by the configured account flow.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
