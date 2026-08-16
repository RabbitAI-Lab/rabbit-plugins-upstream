## Description:

Helps agents search and analyze China procurement and bidding notices, company profiles, competitors, partners, top purchasers, top suppliers, top brands, market aggregates, and price trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, sales teams, and analysts use this skill to query Chinese procurement and bidding data, investigate companies and competitors, and summarize national market activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement queries, company searches, and contact lookups are sent to a third-party procurement data provider.

Mitigation: Use the skill only when that provider may receive the query contents, and review company and contact results before relying on or exporting them.

Risk: First use without an API key can trigger an opt-in registration flow that sends platform, CPU architecture, and a MAC-address hash, then stores an API key in ~/.zlbx/config.json.

Mitigation: Prefer configuring ZLBX_API_KEY before use; if auto-registration is used, obtain user consent before collecting device features and protect the local config file.

Risk: Broad routing for procurement-related prompts can lead the agent to expand company names, retrieve contacts, or surface quota and recharge links during normal analysis.

Mitigation: Review company-name expansions, contact lookups, and quota prompts before sharing results or acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/national-procurement-bidding-net-chinabidding)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON API request examples and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include procurement records, company and contact summaries, aggregate tables, price trends, account status, quota guidance, and links returned by the provider.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
