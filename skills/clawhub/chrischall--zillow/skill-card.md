## Description:

Helps agents find Zillow listings, inspect property details and Zestimates, review market reports, and retrieve a user's saved homes and searches through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home seekers and real-estate researchers use this skill to ask an agent about Zillow listings, property estimates, local market trends, and their saved Zillow activity. It also supports mortgage payment calculations from user-provided inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser bridge access an active Zillow session, including account-linked saved activity.

Mitigation: Verify the npm package and bridge release before installation, and request saved homes or searches only when the user intends to share that information with the agent.

Risk: Zillow access relies on private web endpoints rather than a public consumer API.

Mitigation: Use at your discretion and check important property and market details against Zillow before relying on them.

## Reference(s):

- [Zillow skill on ClawHub](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Text or Markdown summaries of listings, property records, market data, and payment calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved homes and searches require a signed-in Zillow browser session; the skill provides read-only access.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
