## Description:

Routes blockchain data questions to Graph Protocol, Token API, x402, prediction-market, Hyperliquid, and protocol-specific MCP services for live on-chain and market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use Graph Advocate to route blockchain, DeFi, NFT, prediction-market, Hyperliquid, and x402 questions to the relevant Graph Protocol or Graph Advocate service and receive structured live-data responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Blockchain questions, wallet addresses, and trading intent may be sent to graphadvocate.com and related data providers.

Mitigation: Send only non-sensitive queries, avoid private keys, seed phrases, and internal strategy details, and install only if the endpoint operator is trusted.

Risk: Optional x402 paid endpoints can spend USDC when the agent runtime accepts payment challenges.

Mitigation: Start in free or no-wallet mode, require interactive approval for each 402 challenge, use a low-balance wallet, and set per-call and total-spend caps.

Risk: Referenced services may involve Token API keys, JWTs, or GRAPH_API_KEY values.

Mitigation: Store credentials in a secret manager or environment variables, limit their scope, and prevent secrets from appearing in prompts, logs, or shared transcripts.

Risk: The release includes an optional unpinned npm execution path for subgraph-registry-mcp.

Mitigation: Do not run npx subgraph-registry-mcp unless the package version is pinned and audited first.

## Reference(s):

- [ClawHub Graph Advocate Skill Page](https://clawhub.ai/paulieb14/skills/graph-advocate)
- [Aave MCP Reference](references/aave.md)
- [Hyperliquid Reference](references/hyperliquid.md)
- [Polymarket MCP Reference](references/polymarket.md)
- [Subgraph Registry Reference](references/subgraph-registry.md)
- [Token API Reference](references/token-api.md)
- [x402 Payment Analytics Reference](references/x402.md)
- [Graph Advocate Agent Card](https://graphadvocate.com/.well-known/agent-card.json)
- [Graph Advocate Capabilities](https://graphadvocate.com/agents/capabilities.json)
- [Graph Advocate MCP Catalog](https://graphadvocate.com/mcp/catalog)
- [The Graph Studio](https://thegraph.com/studio/)
- [Token API Polymarket Documentation](https://thegraph.com/docs/en/token-api/polymarket-markets/markets/)

## Skill Output:

**Output Type(s):** [text, JSON, guidance, API calls]

**Output Format:** [Structured JSON with concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include route recommendations, query-ready arguments, execution results, get-started links, cache hints, and optional paid endpoint previews.]

## Skill Version(s):

2.11.1 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
