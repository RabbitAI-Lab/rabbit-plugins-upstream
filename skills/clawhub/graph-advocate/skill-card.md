## Description: <br>
Graph Advocate routes plain-English blockchain data questions to Graph Protocol services and returns live data for subgraphs, token activity, DeFi, NFTs, prediction markets, Hyperliquid, x402 analytics, and related MCP packages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulieb14](https://clawhub.ai/user/paulieb14) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Graph Advocate to turn blockchain analytics questions into the right data route, query-ready request, and live response across The Graph, Token API, prediction-market, Hyperliquid, and x402 data sources. It is useful for wallet, token, DeFi, NFT, market, and agent-reputation analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Blockchain questions, wallet addresses, and trading intent are sent to graphadvocate.com. <br>
Mitigation: Avoid sending private keys, seed phrases, confidential strategies, or sensitive internal context; use the skill only when the remote endpoint is trusted for the query. <br>
Risk: Optional x402 paid endpoints can spend USDC when the agent runtime accepts payment challenges. <br>
Mitigation: Start without a wallet; for paid mode, require interactive per-call approval, use a dedicated low-balance wallet, and set per-call and total spend caps. <br>
Risk: Autonomous loops can exhaust free quota or trigger repeated paid calls if payment approval is automated. <br>
Mitigation: Check quota before use and enforce call-count, time, and cost ceilings before each paid request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulieb14/skills/graph-advocate) <br>
- [Graph Advocate homepage](https://github.com/PaulieB14/graph-advocate) <br>
- [Graph Advocate endpoint](https://graphadvocate.com/) <br>
- [Token API reference](references/token-api.md) <br>
- [Subgraph Registry reference](references/subgraph-registry.md) <br>
- [Aave MCP reference](references/aave.md) <br>
- [Polymarket MCP reference](references/polymarket.md) <br>
- [Hyperliquid reference](references/hyperliquid.md) <br>
- [x402 Payment Analytics reference](references/x402.md) <br>
- [The Graph](https://thegraph.com) <br>
- [Subgraph Studio](https://thegraph.com/studio) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON response with routing guidance, query-ready arguments, live execution results, and supporting links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cache hints, get-started links, paid endpoint previews, and x402 payment challenge details when optional paid mode is used.] <br>

## Skill Version(s): <br>
2.9.1 (source: server release evidence and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
