## Description:

Graph Advocate routes plain-English blockchain data questions to Graph Protocol services, Token API endpoints, x402 analytics, prediction-market spread tools, Hyperliquid analytics, and protocol-specific MCP packages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to answer blockchain, DeFi, NFT, prediction-market, Hyperliquid, and x402 settlement questions by selecting the appropriate data service and returning query-ready guidance or live structured data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Blockchain questions, wallet addresses, and possible trading intent are sent to graphadvocate.com and related APIs.

Mitigation: Use the skill only for data you are comfortable sending to those services, and avoid private keys, seed phrases, confidential strategies, or other sensitive private context.

Risk: Paid x402 endpoints can spend USDC when the caller's runtime is configured to accept payment challenges.

Mitigation: Start without a wallet; when paid calls are enabled, use a low-balance wallet, require per-call approval, and configure runtime spend limits.

## Reference(s):

- [Graph Advocate Skill Page](https://clawhub.ai/paulieb14/skills/graph-advocate)
- [Aave MCP Reference](references/aave.md)
- [Hyperliquid Reference](references/hyperliquid.md)
- [Polymarket MCP Reference](references/polymarket.md)
- [Subgraph Registry Reference](references/subgraph-registry.md)
- [Token API Reference](references/token-api.md)
- [x402 Payment Analytics Reference](references/x402.md)
- [The Graph](https://thegraph.com)
- [Subgraph Studio](https://thegraph.com/studio)
- [Token API Polymarket Markets Docs](https://thegraph.com/docs/en/token-api/polymarket-markets/markets/)
- [Graph Advocate Hyperliquid Docs](https://docs.graphadvocate.com/hyperliquid)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown and structured JSON examples with query-ready service recommendations and API call details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live external data, API endpoint selections, tool arguments, cache guidance, and optional x402 payment challenge context.]

## Skill Version(s):

2.10.1 (source: frontmatter, skill.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
