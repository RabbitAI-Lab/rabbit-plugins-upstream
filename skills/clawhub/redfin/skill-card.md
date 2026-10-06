## Description:

Helps agents find Redfin listings, property details, market reports, and signed-in users' saved homes and searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can ask an agent about for-sale properties, property details, local market trends, and their saved Redfin activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser extension can access listing data and saved activity through the user's signed-in Redfin browser session.

Mitigation: Enable the bridge only if comfortable granting this access, and review or install the npm package and extension from trusted sources.

## Reference(s):

- [ClawHub redfin skill](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or text responses with listing details, market figures, and saved-home or saved-search summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; saved activity requires a signed-in Redfin browser session.]

## Skill Version(s):

1.2.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
