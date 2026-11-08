## Description:

Aave V2/V3/V4 MCP server — 51 tools across 16 Graph subgraphs + Aave V4 API + on-chain view contracts. Reserves, positions, cross-chain liquidation risk monitoring with live HF confirmation, governance, V4 hubs/spokes, V4 Base tokenized-stock liquidations, exchange rates, swap quotes, rewards, protocol history, and a durable findings store that survives context compaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use the MCP server to retrieve and analyze Aave market, position, governance, and protocol activity data across supported chains. It also supports monitoring liquidation risk and examining Aave V4 hubs, spokes, rates, and positions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately installed npm package was not audited as part of the supplied skill review.

Mitigation: Review and pin the npm package version before installation.

Risk: The integration requires a Graph API key.

Mitigation: Protect the GRAPH_API_KEY credential.

Risk: The skill describes a persistent findings store, and its storage location and deletion behavior need review.

Mitigation: Check where persistent findings are stored and how to delete them.

## Reference(s):

- [Graph Aave MCP project page](https://github.com/PaulieB14/graph-aave-mcp)
- [Graph Aave MCP on npm](https://www.npmjs.com/package/graph-aave-mcp)
- [The Graph Studio](https://thegraph.com/studio/)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Structured Aave protocol data and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries span multiple chains and Aave versions; reserve queries support symbols, limits, and compact responses.]

## Skill Version(s):

4.3.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
