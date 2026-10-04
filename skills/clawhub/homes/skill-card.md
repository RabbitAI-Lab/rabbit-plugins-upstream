## Description:

Looks up homes.com listings, property details, price and tax history, market reports, saved homes, and photo galleries through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and developers use this skill to research US listings, compare properties, review price and tax history, and access their saved homes and searches.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Using the external package and browser extension requires trust in both components.

Mitigation: Review the package and extension before installation and use only releases you trust.

Risk: Saved homes and searches can expose private data from whichever homes.com account is signed in to the active browser tab.

Mitigation: Confirm the signed-in account before requesting saved data and avoid sharing its results unintentionally.

Risk: Listing and financial details from page content may be incomplete or outdated.

Mitigation: Verify consequential property and cost details against current primary records before acting.

## Reference(s):

- [Homes skill release on ClawHub](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp project source linked in the skill](https://github.com/chrischall/homes-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of property records, histories, market data, and calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Photo links are available in full view; saved homes and searches reflect the active browser account.]

## Skill Version(s):

2.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
