## Description: <br>
DeFi analytics and on-chain execution via Spraay x402 for token prices, swap quotes, wallet profiling, portfolio and NFT holdings, DeFi positions, gas data, ENS resolution, contract reads, swaps, and contract writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to request paid DeFi market, wallet, portfolio, NFT, and contract intelligence through the Spraay x402 gateway. It can also prepare swap execution and contract write calls that require explicit human approval before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses, portfolio data, transaction history, token symbols, and contract call data may leave the local environment through the Spraay gateway. <br>
Mitigation: Install only if the gateway is trusted; avoid sensitive wallets and use a limited test wallet when evaluating the skill. <br>
Risk: Endpoint calls can spend USDC through x402 micropayments. <br>
Mitigation: Review costs and request parameters before each call and keep only limited funds in the agent wallet. <br>
Risk: Swap execution and contract write endpoints can submit irreversible on-chain transactions. <br>
Mitigation: Require explicit human approval, preview swaps with quote/read endpoints first, and verify token, amount, recipient, chain, and slippage before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/plagtech/skills/defi-intelligence-x402) <br>
- [Spraay x402 gateway](https://gateway.spraay.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash and curl. Calls may debit USDC, transmit wallet-related data to an external gateway, and require explicit approval for write endpoints.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter and changelog report 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
