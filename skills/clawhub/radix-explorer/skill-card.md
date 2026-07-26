## Description: <br>
Radix Explorer helps agents query Radix DLT mainnet data for wallets, tokens, validators, transactions, ecosystem updates, DeFi yield pools, dApps, trading venues, and developer resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mavremu](https://clawhub.ai/user/mavremu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and analysts use this skill to look up Radix wallet balances, token data, validator staking information, ecosystem news, DeFi yield information, and related Radix developer resources through the Emily MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses, token addresses, .xrd domains, and related lookup queries are sent to the Emily remote MCP service and its data providers. <br>
Mitigation: Avoid querying wallets, portfolios, domains, or token relationships that are sensitive unless that external-service exposure is acceptable. <br>
Risk: The skill requires installing and using the mcporter npm CLI. <br>
Mitigation: Install the CLI only in environments where adding that dependency is approved, and review the package before deployment. <br>
Risk: Market, wallet, validator, ecosystem, and DeFi data comes from external providers and may be cached, rate limited, or updated on different schedules. <br>
Mitigation: Verify time-sensitive financial, staking, or trading information against authoritative sources before relying on it for decisions. <br>


## Reference(s): <br>
- [Radix Explorer on ClawHub](https://clawhub.ai/mavremu/skills/radix-explorer) <br>
- [Emily](https://www.ineedemily.com) <br>
- [Emily MCP endpoint](https://www.ineedemily.com/api/mcp/mcp) <br>
- [Radix Gateway API](https://docs.radixdlt.com/docs/network-apis) <br>
- [Astrolescent](https://astrolescent.com) <br>
- [CoinMarketCap](https://coinmarketcap.com) <br>
- [Attos Earn](https://earn.attos.world) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with inline shell commands and structured lookup summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the mcporter npm CLI to call a remote Emily MCP service; Radix wallet, token, domain, and related lookup inputs may be sent to external services.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
