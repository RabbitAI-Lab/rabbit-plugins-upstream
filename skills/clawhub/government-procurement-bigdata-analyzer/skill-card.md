## Description:

Helps agents search and analyze Chinese government procurement, public-sector, and state-owned enterprise bidding data for opportunities, awards, companies, competitors, market trends, and price insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, bid teams, sales teams, and market analysts use this skill to retrieve procurement notices, inspect bidder and purchaser history, identify expiring or proposed opportunities, compare competitors, and summarize market and price signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a vendor account and store an API key in a local configuration file.

Mitigation: Prefer configuring ZLBX_API_KEY manually when account control or local secret handling is important, and review local configuration storage before deployment.

Risk: Auto-registration can send a MAC-derived device hash for free-trial device deduplication.

Mitigation: Require explicit user consent before auto-registration, or bypass the flow by preconfiguring an API key.

Risk: Procurement contact phone data may be returned under the service account rules.

Mitigation: Display only service-returned contact data, respect masked contact responses, and avoid supplementing or bulk-exporting phone numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bigdata-analyzer)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries, tables, JSON request examples, shell command snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to procurement records, account-status summaries, and service-returned contact fields subject to account privacy rules.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
