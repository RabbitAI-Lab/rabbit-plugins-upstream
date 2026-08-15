## Description:

招投标大数据搜索 - 招标千里眼 helps agents search, aggregate, and analyze tendering, procurement, company, supplier, buyer, brand, and market trend data using the Zhiliaobiaoxun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business analysts use this skill to query Chinese tendering and bidding data, compare purchasers and suppliers, inspect company procurement activity, analyze competitors, and produce market summaries from API results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and analysis requests are sent to Zhiliaobiaoxun services.

Mitigation: Use the skill only when sending procurement or market-analysis queries to that vendor is acceptable.

Risk: If no API key is configured, the skill can initiate account auto-registration that sends platform, CPU architecture, and a hashed MAC address to the vendor.

Mitigation: Prefer manually configuring ZLBX_API_KEY or ~/.zlbx/config.json before use for clearer control over account creation and device-identification data.

Risk: Auto-registration can store a persistent API key under ~/.zlbx/config.json.

Mitigation: Review local credential storage and remove or rotate the key according to the user's credential-management policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liu-jiapeng/skills/tender-search-qianlima)
- [API Key and Account Portal](https://ai.zhiliaobiaoxun.com/?ch=s22)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Tender Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Automatic Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown summaries, tables, charts, JSON request examples, and shell or configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or local account configuration; may call external Zhiliaobiaoxun services.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
