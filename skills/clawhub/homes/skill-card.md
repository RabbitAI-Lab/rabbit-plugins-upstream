## Description:

Looks up Homes.com listings, property details, price and tax history, market reports, saved homes, and photo galleries through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can ask an agent to research Homes.com listings, compare properties, review price and tax history, and estimate housing costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP package and browser extension can access the Homes.com browser session used for lookups.

Mitigation: Verify package and extension sources or release hashes before installation, and use only an account or session you are comfortable exposing to this integration.

Risk: The skill reads Homes.com pages rather than an official public API, so retrieved details may be incomplete or change when pages change.

Mitigation: Check consequential property details against the live listing before relying on them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses summarizing property data and calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property and photo links may be included; saved-home information requires a signed-in session.]

## Skill Version(s):

2.1.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
