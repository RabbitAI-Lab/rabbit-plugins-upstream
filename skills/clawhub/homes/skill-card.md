## Description:

Helps agents look up homes.com listings, property details, price and tax history, market reports, saved homes, and photos through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents researching US real estate can retrieve homes.com listings, property and market information, saved items, and photos using a browser-connected MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external npm server and browser extension can access homes.com pages available in the signed-in browser session.

Mitigation: Verify that you trust both components before installation and limit use of the signed-in session to appropriate data.

Risk: Scraped listings and calculated housing figures may be incomplete or unsuitable as financial advice.

Mitigation: Check important property and pricing details against authoritative sources; do not treat results as financial advice.

## Reference(s):

- [ClawHub homes skill release](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only property information; photo links require the full view or photo tool.]

## Skill Version(s):

2.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
