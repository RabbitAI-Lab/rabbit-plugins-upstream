## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search and compare Belgian second-hand listings, auctions, and similar items through koopje.ai, then report prices, locations, sources, and links.

### Deployment Geography for Use:

Global; search results focus on Belgian marketplaces and auction sources.

## Known Risks and Mitigations:

Risk: The skill requires a koopje.ai API key and sends search terms, listing URLs, and optional location filters to koopje.ai.

Mitigation: Use the skill only when that data sharing is acceptable, keep the API key secret, and avoid sending sensitive search or location details.

Risk: Saved-listing and own-listing endpoints can change account state by saving, publishing, renewing, or removing listings.

Mitigation: Require explicit user confirmation before account-changing actions, especially before publishing or deleting a listing.

Risk: Search and answer results may be incomplete, rate limited, or empty, and the skill must not invent listings.

Mitigation: Report only listings returned by the API, include source and URL details, and broaden or retry searches only within documented limits.

## Reference(s):

- [koopje.ai /v1 API reference](references/api.md)
- [koopje.ai API](https://koopje.ai/api)
- [koopje.ai agent-readable docs index](https://koopje.ai/llms.txt)
- [ClawHub skill release](https://clawhub.ai/antarcticaice/skills/koopje-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance]

**Output Format:** [Markdown summaries with listing links and optional shell command examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KOOPJE_API_KEY. Search terms, listing URLs, and optional location filters are sent to koopje.ai.]

## Skill Version(s):

1.0.11 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
