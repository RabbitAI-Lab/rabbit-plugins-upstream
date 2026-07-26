## Description: <br>
OKX DEX aggregator (v6). Get swap quotes, swap/approve tx data, tokens, and chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ricky321u](https://clawhub.ai/user/ricky321u) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external agents use this skill to query OKX Wallet DEX API v6 for supported chains, token lists, swap quotes, approval transaction data, and swap transaction payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses OKX API credentials to request DEX quote and transaction data. <br>
Mitigation: Keep OKX secrets out of chat and use least-privilege API credentials where possible. <br>
Risk: Swap and approval payloads can affect wallet assets if signed without review. <br>
Mitigation: Independently verify chain ID, token addresses, spender or router, recipient wallet, amount, allowance, price impact, and slippage before signing any transaction. <br>


## Reference(s): <br>
- [OKX DEX API Reference (v6)](https://web3.okx.com/build/dev-docs/wallet-api/dex-api-reference) <br>
- [ClawHub skill page](https://clawhub.ai/ricky321u/skills/okx-dex) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/ricky321u) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Bash and Python snippets and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, python3, and user-provided OKX API credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
