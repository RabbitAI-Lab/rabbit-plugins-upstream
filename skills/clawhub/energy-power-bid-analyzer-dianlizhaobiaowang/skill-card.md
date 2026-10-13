## Description:

Analyzes Chinese energy and power procurement notices, including bid activity and award concentration for equipment and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts and sales teams search Chinese energy-sector tenders and awards, compare buyers and suppliers, and assess award concentration. Additional company, contact, and cross-industry research is available when specifically requested.

### Deployment Geography for Use:

China (procurement data coverage; no deployment restriction stated)

## Known Risks and Mitigations:

Risk: Automatic account creation transmits hashed device characteristics and stores an API key locally.

Mitigation: Require informed consent before collecting device characteristics or registering; provide an existing API key to bypass registration and protect locally stored credentials.

Risk: Company and procurement research can expose contact details or expand beyond the energy-sector task.

Mitigation: Request contact and broader company research only when needed; preserve masked contacts and avoid bulk contact exports.

Risk: Paid data queries and recharge links can incur costs or prompt account actions.

Mitigation: Review query costs and account status before extended research; use recharge links only when explicitly needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/energy-power-bid-analyzer-dianlizhaobiaowang)
- [Bid search API reference](references/api-search.md)
- [Market analysis API reference](references/api-market.md)
- [Company data API reference](references/api-company.md)
- [Account and usage reference](references/api-account.md)
- [Account registration and privacy workflow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search criteria, dated bid results and monetary amounts when available; requires ZLBX_API_KEY or user-approved account registration.]

## Skill Version(s):

1.0.8 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
