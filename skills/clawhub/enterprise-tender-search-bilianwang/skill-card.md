## Description:

企业级招标采购与供应商寻源助手，用于检索招标、采购和中标公告，核验供应商资质与历史业绩，分析采购市场、竞争对手、价格趋势和潜在客户或供应商。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, bidding, and business development teams use this skill to search Chinese tender and procurement data, inspect company bidding profiles, compare suppliers, analyze market activity, and identify commercial opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically register an account, send device attributes to the provider, and store an API key under ~/.zlbx/config.json.

Mitigation: Prefer a preconfigured ZLBX_API_KEY, and allow automatic registration only after reviewing the provider's device-data collection behavior.

Risk: Generated auto-login recharge links can provide account access for billing or recharge flows.

Mitigation: Treat auto-login links as sensitive account links and avoid sharing them outside the intended user session.

Risk: Company-contact lookup and broad customer-development workflows can surface business contact or prospecting data.

Mitigation: Use the contact and prospecting outputs only for appropriate business purposes and review them before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-tender-search-bilianwang)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Skill overview](artifact/SKILL.md)
- [Tender search API details](artifact/references/api-search.md)
- [Company analysis API details](artifact/references/api-company.md)
- [Market analysis API details](artifact/references/api-market.md)
- [Account query API details](artifact/references/api-account.md)
- [Automatic registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured API request or response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated search criteria, analysis summaries, account-status guidance, and links returned by the provider.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
