## Description:

Provides Aave V2, V3, and V4 market, position, liquidation-risk, governance, and quote data through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Aave markets and positions across chains, compare rates, and investigate liquidation risk using on-chain health-factor checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party npm package requires trusting its publisher and package source.

Mitigation: Verify the npm package source and publisher before installation.

Risk: Supplying unnecessary credentials could expose sensitive access or signing capabilities.

Mitigation: Provide only the Graph API key needed for queries; do not enter private keys or transaction-signing credentials.

## Reference(s):

- [Project homepage](https://github.com/PaulieB14/graph-aave-mcp)
- [npm package](https://www.npmjs.com/package/graph-aave-mcp)
- [The Graph Studio](https://thegraph.com/studio/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aave market and position data, risk analyses, and swap quotes; queries require GRAPH_API_KEY.]

## Skill Version(s):

4.3.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
