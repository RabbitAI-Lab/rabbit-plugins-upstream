## Description:

Searches local Chinese tender and procurement notices by geography, keyword, amount, and date, and supports related company, market, account, and registration API workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and business-development users can search regional Chinese tender notices, inspect bid details, and analyze companies, suppliers, purchasers, brands, pricing, and account usage through a provider API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised as local tender search but also enables broader business intelligence, contact lookup, account handling, device-based registration, and persistent API-key storage.

Mitigation: Review the full tool scope before installation and enable only when the broader procurement and business-intelligence integration is acceptable.

Risk: Auto-registration can send device-derived features to the provider and store a generated API key locally.

Mitigation: Prefer configuring a manually issued ZLBX_API_KEY, and use auto-registration only after explicit user consent.

Risk: Contact lookup and account or billing queries may expose sensitive operational information in shared or regulated environments.

Mitigation: Limit use to authorized users and avoid displaying API keys or unnecessary account details in shared conversations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liu-jiapeng/skills/tender-express-search-bidizhaobiao)
- [Publisher Profile](https://clawhub.ai/user/liu-jiapeng)
- [Skill Definition](artifact/SKILL.md)
- [Tender Search API Reference](artifact/references/api-search.md)
- [Company Analysis API Reference](artifact/references/api-company.md)
- [Market Analysis API Reference](artifact/references/api-market.md)
- [Account API Reference](artifact/references/api-account.md)
- [Auto Registration Reference](artifact/references/auto-register.md)
- [Provider API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Provider API Key Portal](https://ai.zhiliaobiaoxun.com/?ch=s27)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request and response examples plus API-derived text summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or provider configuration; responses may include procurement, company, contact, account, and billing data.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
