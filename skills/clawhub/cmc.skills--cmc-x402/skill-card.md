## Description: <br>
Access CoinMarketCap data via the x402 pay-per-request protocol with USDC payments on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill to integrate CoinMarketCap market data through x402 paid HTTP requests without managing a traditional API key. It covers price quotes, cryptocurrency listings, DEX search, DEX pair data, MCP access, and payment setup guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic paid requests can spend wallet funds when integrations are enabled. <br>
Mitigation: Use a dedicated low-balance hot wallet and review each integration path before enabling automatic paid requests. <br>
Risk: Wallet private keys are required for x402 signing. <br>
Mitigation: Keep private keys in environment variables or a secrets manager, and do not hardcode them in source code. <br>


## Reference(s): <br>
- [x402 Endpoint Reference](references/endpoints.md) <br>
- [x402 Payment Details](references/payment-details.md) <br>
- [x402 Protocol](https://x402.org) <br>
- [x402 Documentation](https://docs.x402.org) <br>
- [CoinMarketCap API Documentation](https://coinmarketcap.com/api/documentation) <br>
- [CoinMarketCap x402 MCP Endpoint](https://mcp.coinmarketcap.com/x402/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TypeScript and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include endpoint URLs, request parameters, and payment configuration details; the skill itself is documentation-only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
