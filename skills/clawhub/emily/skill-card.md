## Description: <br>
Query Radix DLT blockchain data including wallet balances and performance, token prices and market movers, validator staking info, transaction history, network statistics, ecosystem news, DeFi yield pools, XRD trading venues, dApp directory, and developer resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mavremu](https://clawhub.ai/user/mavremu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use Emily to query Radix mainnet wallets, tokens, staking validators, transactions, ecosystem updates, DeFi pools, trading venues, dApps, and developer resources through the configured mcporter integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses, RNS domains, transaction searches, and LP position lookups are sent to Emily's remote MCP service and may be visible to upstream data providers. <br>
Mitigation: Avoid querying wallets, domains, transactions, or portfolio positions that should remain private or that should not be linked to the user's activity. <br>
Risk: Market, DeFi, validator, and ecosystem data may depend on cached or third-party sources and may be incomplete or stale. <br>
Mitigation: Verify important balances, prices, yields, and transaction details against authoritative Radix or provider sources before acting on them. <br>


## Reference(s): <br>
- [Emily](https://www.ineedemily.com) <br>
- [Radix Gateway API](https://docs.radixdlt.com/docs/network-apis) <br>
- [Astrolescent](https://astrolescent.com) <br>
- [CoinMarketCap](https://coinmarketcap.com) <br>
- [Attos Earn](https://earn.attos.world) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and natural-language responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses mcporter to call a remote Radix MCP service; no API key is required, and documented calls are mainnet-only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
