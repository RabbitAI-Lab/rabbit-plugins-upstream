## Description:

Graph Advocate routes plain-English blockchain data questions to The Graph services, Token API, protocol-specific MCP packages, and optional paid analytics endpoints so agents can retrieve live onchain and market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to route blockchain, DeFi, NFT, prediction-market, Hyperliquid, x402, and agent-reputation questions to the appropriate data service and return structured results or query-ready guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Blockchain questions, wallet addresses, and trading intent may be sent to graphadvocate.com and related data providers.

Mitigation: Install only if the endpoint operator is trusted, avoid sending private keys or sensitive strategy context, and treat wallet or trading details as potentially exposed to the remote service.

Risk: Optional x402 endpoints can spend USDC when an agent runtime accepts payment challenges.

Mitigation: Keep payment approval interactive, use a dedicated low-balance wallet, check free quota before paid calls, and enforce per-call and total spend caps.

Risk: Token API or Graph API credentials used with related services could be exposed if placed in prompts or logs.

Mitigation: Store credentials in a proper secret store and avoid including secrets in prompts, transcripts, or generated output.

## Reference(s):

- [Graph Advocate GitHub](https://github.com/PaulieB14/graph-advocate)
- [Subgraph Registry Reference](references/subgraph-registry.md)
- [Token API Reference](references/token-api.md)
- [Aave MCP Reference](references/aave.md)
- [Polymarket MCP Reference](references/polymarket.md)
- [Hyperliquid Reference](references/hyperliquid.md)
- [x402 Payment Analytics Reference](references/x402.md)
- [The Graph Token API Polymarket Docs](https://thegraph.com/docs/en/token-api/polymarket-markets/markets/)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls, Configuration]

**Output Format:** [JSON responses with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include service recommendations, query arguments, execution results, cache guidance, free-tier links, and payment-challenge details for opt-in paid endpoints.]

## Skill Version(s):

2.11.1 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
