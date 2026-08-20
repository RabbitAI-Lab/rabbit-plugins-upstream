## Description:

Simulate a Uniswap swap before making it - amount out, effective price, price impact - computed offline from The Graph with the protocol's own concentrated-liquidity math, plus pools, token prices, pair lookup, and live swap flow across Uniswap V2/V3/V4 on Ethereum, Arbitrum, Base, Polygon, Optimism, and BSC.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and DeFi users use this skill to answer Uniswap swap, pool, token price, liquidity, and recent-trade questions with data from The Graph. It helps estimate single-pool swap outcomes and price impact before a user treats the result as market information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP process receives a Graph API key and makes The Graph queries from the user's environment.

Mitigation: Install only when that credential exposure and network behavior are acceptable; scope and rotate the API key according to the user's security practices.

Risk: Swap quotes are informational and may differ from executable prices because real execution depends on chain state at inclusion.

Mitigation: Present quote outputs as estimates, report non-quotable reasons, and recommend on-chain quoting or execution checks for material trades.

Risk: Using npx without a pinned package can reduce reproducibility across installs.

Mitigation: Pin the npm package version when reproducible runtime behavior is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/graph-uniswap)
- [Graph Uniswap homepage](https://github.com/PaulieB14/graph-uniswap-mcp)
- [The Graph Studio](https://thegraph.com/studio)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Plain text or Markdown summaries of Uniswap market data, swap quotes, token prices, pool information, and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GRAPH_API_KEY for The Graph queries; quote results are informational and depend on the most recently indexed subgraph state.]

## Skill Version(s):

0.3.1 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
