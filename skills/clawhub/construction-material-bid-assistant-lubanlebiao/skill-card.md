## Description:

查询建材、钢材、管材和机械相关的招采信息，提供历史中标单价、品牌趋势及主要供应商信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and suppliers use this skill to research Chinese construction-material bid notices, historical unit prices, leading brands and potential vendors. It also offers broader procurement and company intelligence when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query broader procurement intelligence and company contacts beyond material pricing.

Mitigation: Limit lookups to the user's requested task; review contact details before sharing them.

Risk: Automatic account registration sends a hashed device identifier and stores an API key locally.

Mitigation: Prefer a user-provided key through the platform's secret mechanism; obtain consent before registration and review the local key file.

Risk: Queries may consume credits, and account flows can generate recharge links.

Mitigation: Check charges before repeated queries and confirm any recharge link before using it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/construction-material-bid-assistant-lubanlebiao)
- [Market analysis and price tools](artifact/references/api-market.md)
- [Bid search API](artifact/references/api-search.md)
- [Company registry tools](artifact/references/api-registry.md)
- [Account registration and key handling](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries with tables and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search filters, dates and monetary units when available.]

## Skill Version(s):

1.0.8 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
