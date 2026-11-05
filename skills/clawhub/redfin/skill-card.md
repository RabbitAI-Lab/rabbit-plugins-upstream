## Description:

Look up Redfin listings, property details, market reports, and saved homes or searches through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can search Redfin listings, review property and market details, check climate risks, and view their saved homes or searches. They can also calculate an estimated monthly mortgage payment from supplied figures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and searches from the signed-in Redfin account become available to the agent.

Mitigation: Use the skill only with an agent setup and browser session you trust, and review the external dependencies before connecting the account.

Risk: The skill depends on external npm and browser-extension packages, and Redfin's private endpoints may change or stop working.

Mitigation: Pin the npm version, verify the extension download, and review both dependencies; confirm results in Redfin if lookups fail or appear stale.

## Reference(s):

- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp project repository](https://github.com/chrischall/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge project](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension reference](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Text, Structured data, Calculations]

**Output Format:** [Natural-language text and structured property, market, and calculation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property and account lookups are read-only; saved-home and saved-search results require an authenticated Redfin browser session.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
