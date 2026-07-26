## Description: <br>
Query Radix DLT blockchain data including wallet balances and performance, token prices and market movers, validator staking info, transaction history, network statistics, ecosystem news, DeFi yield pools, XRD trading venues, dApp directory, and developer resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mavremu](https://clawhub.ai/user/mavremu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and analysts use this skill to look up Radix mainnet wallet, token, validator, DeFi, ecosystem, and developer-resource information through the Emily Radix assistant service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires the mcporter npm package, which introduces normal package supply-chain trust considerations. <br>
Mitigation: Install mcporter only from a trusted npm source and use normal dependency review practices before enabling the skill. <br>
Risk: Wallet addresses, .xrd domains, token identifiers, and market or DeFi queries may be sent to the Emily service and listed data providers. <br>
Mitigation: Avoid submitting addresses or queries considered personally sensitive unless the user trusts those services. <br>
Risk: The skill returns market, DeFi, and blockchain data from third-party or cached sources that may be delayed or incomplete. <br>
Mitigation: Treat returned values as informational lookup results and verify important financial or operational decisions against authoritative sources. <br>


## Reference(s): <br>
- [Emily Radix Assistant](https://www.ineedemily.com) <br>
- [Emily MCP Endpoint](https://www.ineedemily.com/api/mcp/mcp) <br>
- [Radix Gateway API Documentation](https://docs.radixdlt.com/docs/network-apis) <br>
- [Astrolescent](https://astrolescent.com) <br>
- [CoinMarketCap](https://coinmarketcap.com) <br>
- [Attos Earn](https://earn.attos.world) <br>
- [ClawHub Skill Page](https://clawhub.ai/mavremu/skills/emily-radix-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with command examples and API-derived lookup results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mainnet-only Radix data; the service documents a 60 requests per minute per IP rate limit.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
