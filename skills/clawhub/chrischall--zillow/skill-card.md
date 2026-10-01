## Description:

Helps agents look up Zillow property listings, Zestimates, saved homes and searches, and market reports through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People searching for homes and agents assisting them can retrieve Zillow listings, property details, market trends, and signed-in saved activity, or estimate mortgage payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the service routes Zillow queries through a signed-in browser session and requires third-party software.

Mitigation: Install the MCP package and browser extension only if you trust them and are comfortable using your Zillow session.

Risk: Saved-home and saved-search results can reveal private Zillow account activity.

Mitigation: Request saved activity only when needed and avoid sharing those results beyond the intended audience.

## Reference(s):

- [Zillow skill on ClawHub](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language property and market summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing URLs, prices, Zestimates, saved-account activity, and mortgage payment breakdowns.]

## Skill Version(s):

1.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
