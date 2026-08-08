## Description:

Route any blockchain data question to the right Graph Protocol service and return live data from subgraphs, Token API, x402 analytics, prediction-market spread routes, Hyperliquid routes, and protocol-specific MCP packages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulieb14](https://clawhub.ai/user/paulieb14)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to route plain-English blockchain data questions to appropriate Graph Protocol, Token API, Polymarket, Hyperliquid, Aave, x402, and related data services. It helps agents produce query-ready requests, live data responses, and setup guidance for supported free and opt-in paid endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Blockchain questions, wallet addresses, and possible trading intent are sent to graphadvocate.com and related data providers.

Mitigation: Use the skill only when that disclosure is acceptable, and do not submit private keys, seed phrases, API keys, confidential strategy details, or other sensitive private context.

Risk: Opt-in x402 endpoints can settle paid USDC requests when the caller runtime accepts payment challenges.

Mitigation: Keep paid mode interactive, review each 402 challenge before signing, use a dedicated low-balance wallet, set per-call and total spend caps, and check free-quota status before paid calls.

Risk: Optional external MCP packages and upstream services may have separate trust, credential, and versioning requirements.

Mitigation: Audit optional packages separately, pin known versions, provide only the required credentials such as GRAPH_API_KEY, and use embedded reference tables when remote reference data conflicts with the installed skill.

## Reference(s):

- [Aave MCP Reference](references/aave.md)
- [Hyperliquid Reference](references/hyperliquid.md)
- [Polymarket MCP Reference](references/polymarket.md)
- [Subgraph Registry Reference](references/subgraph-registry.md)
- [Token API Reference](references/token-api.md)
- [x402 Payment Analytics Reference](references/x402.md)
- [Graph Advocate Agent Card](https://graphadvocate.com/.well-known/agent-card.json)
- [Graph Advocate MCP Catalog](https://graphadvocate.com/mcp/catalog)
- [The Graph Studio](https://thegraph.com/studio/)
- [Token API Polymarket Documentation](https://thegraph.com/docs/en/token-api/polymarket-markets/markets/)
- [Graph Advocate Hyperliquid Documentation](https://docs.graphadvocate.com/hyperliquid)

## Skill Output:

**Output Type(s):** [Text, JSON, API Calls, Configuration, Guidance]

**Output Format:** [Structured JSON responses with query-ready tool arguments, live data payloads when available, and concise explanatory text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include service recommendations, confidence, execution results, get-started links, cache duration, free-quota information, and opt-in x402 payment challenge details.]

## Skill Version(s):

2.9.2 (source: frontmatter, skill.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
