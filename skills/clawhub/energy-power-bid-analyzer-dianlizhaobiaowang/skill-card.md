## Description:

Analyzes Chinese energy and power procurement notices, including grid, solar, storage, and wind projects, to identify purchasing patterns and award concentration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and market analysts search Chinese energy-sector tenders and awards, compare buyers and suppliers, and assess concentration in equipment or engineering contracts. The skill also supports related company, contact, market, and account queries when requested.

### Deployment Geography for Use:

Global (covers Chinese procurement data)

## Known Risks and Mitigations:

Risk: First-use account creation may collect hashed MAC and device features and store an API key locally.

Mitigation: Review the data collection before installation; supply your own ZLBX_API_KEY to avoid automatic registration, or consent explicitly before registering.

Risk: Company, contact, and account lookups go beyond the energy-focused title and may expose sensitive business or contact information.

Mitigation: Use these features only when needed for the procurement task, and avoid bulk contact export or attempts to unmask contact details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/energy-power-bid-analyzer-dianlizhaobiaowang)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search reference](references/api-search.md)
- [Company analysis reference](references/api-company.md)
- [Market analysis reference](references/api-market.md)
- [Company registry reference](references/api-registry.md)
- [Account reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with links to source notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the queried data and account access; missing fields should not be invented.]

## Skill Version(s):

1.0.9 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
