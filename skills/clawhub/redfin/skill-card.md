## Description:

Looks up Redfin home listings, property details, market reports, and a user's saved homes and searches through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home shoppers and real-estate professionals use this skill to explore listings, compare property details and market trends, estimate mortgage payments, and review their own saved Redfin activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser integration can access a signed-in Redfin session and private saved homes and searches.

Mitigation: Enable it only if comfortable granting session access, and explicitly request retrieval of saved account data.

Risk: Installation pulls an external MCP package and browser extension.

Mitigation: Review the package and extension source or verify release checksums before installing.

## Reference(s):

- [Redfin skill listing](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with property and market data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property and saved-activity tools can return compact or full details.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
