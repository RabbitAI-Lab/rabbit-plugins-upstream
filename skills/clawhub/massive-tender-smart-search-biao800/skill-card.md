## Description:

Helps agents search and analyze Biao800/Zhiliaobiaoxun tender, bid, company, and market data using precise keyword, exclusion, amount, date, and region filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business-development teams use this skill to find tender opportunities, inspect bid details, analyze companies and competitors, and summarize market activity from vendor-hosted tender data. It is suited for precise search workflows that combine keywords, exclusions, regions, dates, and amount filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a vendor account and store an API key under ~/.zlbx/config.json.

Mitigation: Prefer preconfiguring ZLBX_API_KEY; require user consent before auto-registration; never expose API keys in responses.

Risk: Auto-registration sends platform, CPU architecture, and a hashed MAC address for device de-duplication.

Mitigation: Only proceed after user consent; skip auto-registration by configuring ZLBX_API_KEY or an existing local config; do not collect hostnames, usernames, home paths, file contents, or raw MAC addresses.

Risk: Contact lookup may return phone numbers, and bulk outreach can create privacy or compliance risk.

Mitigation: Display contact data only as returned, respect masked contact privacy, and do not supplement, de-anonymize, or batch export contacts.

Risk: Tender and company analysis can be incomplete or misleading if filters, money units, or vendor data are wrong.

Mitigation: State the applied filters, use the documented unit conversions, avoid inventing missing fields, and verify important business decisions against source records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)
- [Publisher profile](https://clawhub.ai/user/pkuycl)
- [Skill instructions and API overview](SKILL.md)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun data API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples and links to tender or company records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include REST request details and account or quota guidance; results depend on the configured ZLBX_API_KEY and vendor API responses.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
