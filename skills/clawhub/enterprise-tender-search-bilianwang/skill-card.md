## Description:

An enterprise procurement assistant for searching tender, procurement, award, supplier, competitor, company, market, and pricing data through the Zhiliaobiaoxun/Bilianwang API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, sales, and analyst users use this skill to find Chinese tender opportunities, verify suppliers, analyze company bidding activity, identify competitors, and summarize procurement market trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement, supplier, company, and market queries are sent to a third-party data provider.

Mitigation: Install only if this data sharing is acceptable, and avoid sending confidential procurement strategy or sensitive company information unless approved.

Risk: Automatic account setup uses device characteristics for trial-account deduplication and may store an API key in ~/.zlbx/config.json.

Mitigation: Prefer setting ZLBX_API_KEY manually when possible, require user consent before auto-registration, and protect ~/.zlbx/config.json as a secret file.

Risk: Auto-login or recharge links can grant account access during their validity window.

Mitigation: Do not share generated login or recharge links, and regenerate them only when the user requests a fresh link.

Risk: Aggregated procurement records and fuzzy company matching can be misleading if the entity scope is wrong.

Mitigation: Verify matched company names, subsidiary coverage, time windows, amount units, and source records before relying on results for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-tender-search-bilianwang)
- [Procurement data API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s49)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration]

**Output Format:** [Markdown responses with tables, JSON request examples, REST API calls, and occasional shell commands for credential setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or user-approved auto-registration before data access.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
