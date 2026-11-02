## Description:

Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP. Triggers on phrases like "find homes on redfin in", "redfin property details for", "show my saved redfin homes", "what's my saved redfin search seeing", "what does redfin say about", "redfin market report for", or any request involving Redfin properties, prices, or your saved Redfin activity. Requires redfin-mcp installed and the ContextMint Bridge extension active (see Setup below).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home shoppers, property owners, and market researchers use the skill to search Redfin listings, review property and regional market details, estimate mortgage payments, and inspect saved homes or searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in Redfin lookups can expose saved homes and searches from the active Redfin session.

Mitigation: Install only if you trust redfin-mcp and the browser extension; verify the extension download and review pairing permissions.

Risk: The skill uses unofficial Redfin endpoints that may change.

Mitigation: Prefer a reviewed package version and expect the lookups to stop working if Redfin changes those endpoints.

## Reference(s):

- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp project information](https://github.com/chrischall/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge project](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Property and market data, Guidance]

**Output Format:** [Natural-language summaries with structured listing, property, market, and mortgage data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; saved-account results require an active signed-in Redfin session.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
