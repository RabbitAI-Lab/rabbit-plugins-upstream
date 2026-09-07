## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, compare, and price Belgian second-hand listings and auction lots through the koopje.ai API, then report listing URLs, prices, locations, and sources to users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, listing URLs, and optional postcode or coordinate filters are sent to koopje.ai.

Mitigation: Use the skill only when this data sharing is acceptable, and prefer less precise location filters unless exact distance is needed.

Risk: The skill requires a KOOPJE_API_KEY for authenticated API access.

Mitigation: Keep the API key private, provide it through the environment, and rotate it if it may have been exposed.

Risk: Marketplace and auction results may be missing, stale, rate limited, or unavailable if the API request fails.

Mitigation: Use the documented status and error handling guidance, retry once after rate limiting, and avoid inventing listings when the API returns no results.

## Reference(s):

- [koopje.ai API reference](references/api.md)
- [koopje.ai](https://koopje.ai)
- [ClawHub skill page](https://clawhub.ai/antarcticaice/skills/koopje-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with listing links and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request examples, search result summaries, listing URLs, prices, locations, sources, and connectivity or error guidance.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
