## Description:

Helps agents find Redfin property listings, property details, market reports, and a signed-in user's saved homes and searches through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home seekers and real-estate professionals use this skill to ask an agent about Redfin listings, property details, local market trends, mortgage estimates, and their saved homes or searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to saved homes and searches exposes personal Redfin account data.

Mitigation: Use saved-account tools only with the user's consent and limit sharing of their results.

Risk: The MCP server and browser extension use the user's signed-in Redfin session.

Mitigation: Verify the npm package and ContextMint Bridge release before installation and use a trusted signed-in session.

## Reference(s):

- [ClawHub redfin release](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language answers based on structured property and market data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved-home and saved-search results require an authenticated Redfin session; property results may include links and prices.]

## Skill Version(s):

1.2.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
