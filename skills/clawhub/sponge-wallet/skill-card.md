## Description: <br>
Sponge Wallet manages crypto wallet balances, token transfers, Solana swaps, transaction history, funding requests, withdrawals, and paid API access through x402 micropayments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rishabluthra](https://clawhub.ai/user/rishabluthra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect wallet balances, prepare or execute token transfers and swaps, request or withdraw funds, and access paid web, image, prediction-market, scraping, document-parsing, and prospecting APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can authorize an agent to transfer funds, swap tokens, withdraw balances, sign x402 payments, and auto-pay APIs. <br>
Mitigation: Use test keys or low-balance wallets, confirm recipient, chain, token, amount, slippage, and payment recipient before every state-changing action, and set auto_pay=false when reviewing paid API costs. <br>
Risk: Stored or environment-provided Sponge credentials grant wallet and payment authority to the agent while active. <br>
Mitigation: Prefer scoped credentials, avoid sharing live keys, log out or rotate credentials after use, and keep stored credentials protected. <br>
Risk: Overriding SPONGE_API_URL can redirect wallet and payment traffic to an untrusted service. <br>
Mitigation: Use the default API endpoint unless the alternate endpoint is fully trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rishabluthra/skills/sponge-wallet) <br>
- [Tool parameter reference](REFERENCE.md) <br>
- [Skill documentation](SKILL.md) <br>
- [Sponge Wallet API endpoint](https://api.wallet.paysponge.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [JSON tool responses with Markdown command examples and parameter documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [State-changing wallet and paid API actions require Sponge credentials and may return transaction, balance, payment, or API result data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
