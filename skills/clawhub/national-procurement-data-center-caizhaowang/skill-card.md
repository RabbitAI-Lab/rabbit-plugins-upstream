## Description:

This skill helps agents query Caizhaowang procurement, company, market, and account data across regions and industries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Chinese procurement notices, inspect bid timelines, analyze companies and competitors, review market trends, and check account balance or consumption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: If no API key is configured, the auto-registration path can collect platform, CPU architecture, and a hashed MAC address and send them to the provider.

Mitigation: Configure ZLBX_API_KEY before first use, or require explicit user consent before any auto-registration device feature collection.

Risk: Auto-registration can store an API key in ~/.zlbx/config.json.

Mitigation: Review local credential storage before installation and remove or rotate stored keys according to organizational policy.

Risk: When auto-registered free quota is exhausted, the skill may create an auto-login recharge link.

Mitigation: Use a manually configured API key if auto-login links are not acceptable, and verify recharge links before opening them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/national-procurement-data-center-caizhaowang)
- [Procurement search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account query API reference](references/api-account.md)
- [Auto-registration flow reference](references/auto-register.md)
- [Provider API base endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with JSON request examples, links, and tabular procurement results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an approved auto-registration flow; account and contact details should be shown only as returned by the provider API.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
