## Description:

权威采招政策与标讯指南-元博网用于查询大型基础设施项目、重点政企采购和标讯驱动的宏观趋势，并生成结构严谨、数据翔实的市场简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement analysts, and business development teams use this skill to search bid notices, analyze companies, inspect procurement timelines, and summarize market trends from Yuanbowang/Zhiliaobiaoxun data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic vendor onboarding can create an account, send a persistent device-derived identifier, and store an API key locally.

Mitigation: Prefer preconfiguring ZLBX_API_KEY; require user consent before auto-registration; disclose the device features sent and where the API key is stored.

Risk: Vendor notices, recharge links, and recommendations may be appended to normal answers.

Mitigation: Present these as vendor-provided content and keep procurement analysis separate from account or recharge guidance.

Risk: The skill depends on a vendor API key and external procurement data APIs, so output quality depends on service availability, account quota, and returned data.

Mitigation: Check account status when relevant, report API errors plainly, and avoid fabricating missing bid, company, contact, or market data.

## Reference(s):

- [Skill API overview](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance]

**Output Format:** [Markdown with tables, summaries, links, and inline JSON or HTTP examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bid search results, company profiles, market aggregations, account status, and vendor onboarding guidance.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
