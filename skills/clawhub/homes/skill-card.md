## Description:

Helps agents look up homes.com listings, property details, price and tax history, market reports, saved homes, and photo galleries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can ask an agent to research US homes.com listings, compare properties, review market and property history, or inspect saved homes and searches.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The external MCP package and browser extension can read homes.com pages and saved information visible in the signed-in browser session.

Mitigation: Install only if this access is acceptable, and verify the package and extension sources or checksums before installation.

## Reference(s):

- [Homes skill on ClawHub](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp package](https://www.npmjs.com/package/homes-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses with structured property and market details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Photo URLs are available when requested; some listing results may be truncated.]

## Skill Version(s):

2.1.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
