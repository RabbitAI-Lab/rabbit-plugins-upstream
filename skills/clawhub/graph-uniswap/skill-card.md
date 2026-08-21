## Description:

Simulates Uniswap swaps and answers pool, token price, liquidity, fee tier, and recent swap questions using The Graph data across Uniswap V2, V3, and V4 on supported EVM chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to evaluate Uniswap pools, prices, and single-pool swap quotes before deciding whether to perform further on-chain validation or execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends GraphQL queries to The Graph using the configured Graph API key.

Mitigation: Use an appropriate scoped API key and avoid providing wallet keys or unrelated secrets.

Risk: Swap quotes are informational and can differ from execution because markets move and subgraph data can lag.

Mitigation: Treat material quotes as pre-trade analysis and validate current execution conditions before acting.

Risk: Some pools or trade sizes are not safely quotable, including hook-driven V4 pools, zero in-range liquidity, and trades larger than visible liquidity.

Mitigation: Report the skill's unquotable reason instead of substituting a guess or TVL estimate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/graph-uniswap)
- [Project homepage](https://github.com/PaulieB14/graph-uniswap-mcp)
- [The Graph Studio](https://thegraph.com/studio)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with command examples and structured tool-selection guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GRAPH_API_KEY; results are read-only informational market data and swap simulations, not trade execution.]

## Skill Version(s):

0.3.3 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
