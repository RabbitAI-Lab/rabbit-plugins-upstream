## Description:

Helps users search Chinese bidding records and analyze buyers, suppliers, competitors, market trends, and potential opportunities through the 知了标讯 data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and sales analysts use this skill to find Chinese tender notices, compare buyer and supplier activity, assess competitors, and summarize market trends or opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration sends device-derived identifiers to an external service.

Mitigation: Request informed consent before registration; supply an existing ZLBX_API_KEY to avoid automatic registration.

Risk: An automatically obtained API key is persisted locally and could be exposed.

Mitigation: Prefer an existing key supplied through the environment; protect any locally stored key and never include it in responses.

Risk: Some data queries consume account credits and contact records may contain personal information.

Mitigation: Limit queries to the requested scope, check credit use, and retain masked contact information without attempting to reconstruct or bulk-export it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform)
- [Bidding search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Company registry API reference](references/api-registry.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries, tables, and links to bidding records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an external bidding-data API; some queries consume account credits.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
