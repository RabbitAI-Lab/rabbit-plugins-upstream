## Description:

Look up Zillow listings, property details, Zestimates, saved searches and homes, and market reports through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers, owners, or real-estate researchers use it to search listings, inspect property details and estimate history, review market conditions, and check saved searches or favorite homes. It can also calculate local mortgage estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-based access can expose signed-in Zillow saved activity to the agent.

Mitigation: Use it only if comfortable sharing that activity through the browser session.

Risk: The skill scan does not fully audit its external package and browser extension dependencies.

Mitigation: Pin the npm version, verify the extension download, and review its permissions.

## Reference(s):

- [zillow-mcp package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Structured property, market, saved-activity, and mortgage results, presented as text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include property image URLs and user-specific saved searches or favorite homes.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
