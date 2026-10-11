## Description:

Helps agents search Compass real-estate listings, inspect property details and history, compare homes, and estimate mortgage payments through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and their agents can look up Compass listings, photos, price histories, comparable properties, and estimated housing costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses a signed-in Compass browser session and a separately installed MCP package and browser extension.

Mitigation: Trust and verify the compass-mcp package and ContextMint Bridge extension before installation, and use a browser session you intend to share for lookups.

Risk: Listing availability, prices, and calculated affordability can be incomplete or change over time.

Mitigation: Check current property details with Compass and independently verify estimates before making financial decisions.

## Reference(s):

- [Compass skill on ClawHub](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown with listing details, comparisons, links, and estimated calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property results depend on the signed-in Compass session; mortgage and affordability estimates are calculated locally.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
