## Description:

Helps agents query Booli for Swedish property areas, for-sale and sold listings, and property details using browser-backed shell commands without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up Swedish property areas, compare current and sold listings, and retrieve property details from a shell without running the Booli MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated Booli requests are relayed through a browser session that has passed Cloudflare checks.

Mitigation: Review Booli's terms before automating and limit the extension's site access to booli.se.

Risk: Browser pairing and the fpx profile remain available after initial approval.

Mitigation: Remove the pairing and profile when they are no longer needed.

## Reference(s):

- [Booli GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell examples and GraphQL JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices in SEK and floor areas in m²; check the response for GraphQL errors.]

## Skill Version(s):

2.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
