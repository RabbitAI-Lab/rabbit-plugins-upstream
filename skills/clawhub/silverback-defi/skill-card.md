## Description: <br>
DeFi intelligence powered by Silverback for 19 x402-paid endpoints on Base chain, covering market data, swap quotes, technical analysis, yield opportunities, token audits, whale tracking, and AI chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ridingliquid](https://clawhub.ai/user/ridingliquid) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to call Silverback DeFi endpoints for Base-chain market intelligence, trading analysis, yield discovery, token risk checks, and x402-paid AI chat. It is intended for users comfortable reviewing wallet payments and independently verifying DeFi actions before signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid DeFi API calls can spend USDC through x402 payment flows. <br>
Mitigation: Use a limited-balance wallet and confirm each 402 charge before payment. <br>
Risk: Swap and Permit2 signing requests can affect wallet assets. <br>
Mitigation: Independently verify every swap quote, token address, and Permit2 request before signing. <br>
Risk: The optional MCP npm package is separate executable software. <br>
Mitigation: Review and trust the package before installing it globally. <br>


## Reference(s): <br>
- [Silverback DeFi website](https://silverbackdefi.app) <br>
- [Silverback x402 documentation](https://silverbackdefi.app/x402) <br>
- [Silverback x402 API](https://x402.silverbackdefi.app) <br>
- [silverback-x402-mcp npm package](https://www.npmjs.com/package/silverback-x402-mcp) <br>
- [ClawHub skill page](https://clawhub.ai/ridingliquid/skills/silverback-defi) <br>
- [Publisher profile](https://clawhub.ai/user/ridingliquid) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl examples, endpoint descriptions, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may involve x402 USDC payments and may return unsigned EIP-712 Permit2 data for client-side signing.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
