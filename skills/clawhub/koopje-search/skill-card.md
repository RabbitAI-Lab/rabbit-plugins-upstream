## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find, compare, price, and inspect Belgian second-hand listings and auction lots through the koopje.ai API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a koopje.ai API key and can send search queries and optional location data to koopje.ai.

Mitigation: Use the minimum query and location detail needed, keep the API key secret, and tell users when requests depend on koopje.ai.

Risk: The documentation includes saved-item and own-listing endpoints that can change account state or publish, renew, or remove public listings.

Mitigation: Use read-only search, similar, answer, contents, and stats endpoints by default; require explicit user confirmation before any save, remove, publish, renew, or listing creation action.

Risk: Marketplace and auction results can be stale, incomplete, or have no fixed sale price.

Mitigation: Report the source URL, price text, location, and source for each result; for auction lots, clearly state that no fixed price is available.

## Reference(s):

- [koopje.ai /v1 API reference](references/api.md)
- [Koopje API](https://koopje.ai)
- [Koopje agent-readable documentation index](https://koopje.ai/llms.txt)
- [ClawHub skill page](https://clawhub.ai/antarcticaice/skills/koopje-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with listing links, JSON examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a KOOPJE_API_KEY credential and returns API-backed marketplace results with source URLs.]

## Skill Version(s):

1.0.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
