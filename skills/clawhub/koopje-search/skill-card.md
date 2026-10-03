## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and assistants search and compare Belgian second-hand listings and auction lots, check listing details, and share prices, locations, sources, and links.

### Deployment Geography for Use:

Global (focused on Belgian marketplace listings)

## Known Risks and Mitigations:

Risk: A search-focused skill also provides actions that change saved items and public listings.

Mitigation: Treat searches as read-only; require explicit confirmation before saving or removing items, creating drafts, publishing or renewing ads, or removing listings.

Risk: The API key may grant broader account access than search, and precise location may be disclosed.

Mitigation: Use a key only if its account permissions are acceptable, keep it private, and confirm before sending precise latitude and longitude.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/antarcticaice/skills/koopje-search)
- [Koopje API reference](references/api.md)
- [Koopje API and MCP setup](https://koopje.ai/api#mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with listing links and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should identify prices, locations, and original sources; auction lots may not have fixed prices.]

## Skill Version(s):

1.0.16 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
