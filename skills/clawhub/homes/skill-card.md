## Description:

Helps agents explore homes.com listings, property records, market reports, saved homes, and photos through a browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and their agents can search and compare homes.com properties, review price and tax history, inspect market reports and photos, and retrieve saved homes or searches from a signed-in account.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The external homes-mcp package and ContextMint Bridge extension access listing data through the active browser session.

Mitigation: Review and trust both components before installation, and use only a browser session you intend to share with the agent.

Risk: Saved-home and saved-search requests can expose data from the account signed in to the active homes.com tab.

Mitigation: Confirm the signed-in account and request saved data only when it is needed.

## Reference(s):

- [ClawHub homes skill release](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp package](https://www.npmjs.com/package/homes-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with property details, comparisons, calculations, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Photo URLs require the photo tool or full view; saved homes and searches require a signed-in homes.com tab.]

## Skill Version(s):

2.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
