## Description:

This skill helps agents search and analyze Chinese procurement and bidding notices, company bidding profiles, competitor activity, purchaser and supplier rankings, brand and model price trends, and market aggregates through Zhiliaobiaoxun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill through an agent to search Chinese procurement and bidding data, inspect company participation, identify competitors or potential suppliers, and produce concise market summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement queries are sent to a third-party service.

Mitigation: Use the skill only when the vendor may process the query content, and avoid submitting confidential procurement or account data unless permitted.

Risk: Auto-registration may collect a MAC-derived device hash and store an API key locally.

Mitigation: Prefer configuring ZLBX_API_KEY manually; if auto-registration is used, require explicit user consent and protect ~/.zlbx/config.json.

Risk: The skill may display service-provided notices, promotional links, or auto-login links.

Mitigation: Review links before opening or sharing them, and use only expected Zhiliaobiaoxun domains for account and recharge workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/national-procurement-bidding-net-chinabidding)
- [Search API Reference](references/api-search.md)
- [Company API Reference](references/api-company.md)
- [Market API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with tables, JSON or HTTP request examples, and optional shell commands for account setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-consented auto-registration; may store an API key in ~/.zlbx/config.json.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
