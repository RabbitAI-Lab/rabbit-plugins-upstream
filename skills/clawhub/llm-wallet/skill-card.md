## Description: <br>
Manage crypto wallets and make x402 micropayments with USDC stablecoins on Polygon. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akshatgada](https://clawhub.ai/user/akshatgada) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to let agents create and manage encrypted wallets, check balances, set spending limits, and make user-approved x402 USDC micropayments to paid APIs on Polygon. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-initiated payments can transfer value on mainnet or to an unintended endpoint. <br>
Mitigation: Start on polygon-amoy testnet, set low per-transaction and daily limits, and review the exact URL, amount, network, and recipient before approving any payment. <br>
Risk: Wallet private keys or encryption keys exposed in chat, logs, or shell history can compromise funds. <br>
Mitigation: Avoid production private keys, keep keys out of chat and logs, and store wallet secrets in environment variables or a secure secret store. <br>
Risk: Repeated paid API calls can consume a user's budget. <br>
Mitigation: Use pre-flight payment checks, require user approval for paid calls, and monitor transaction history and remaining daily limits. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/akshatgada/skills/llm-wallet) <br>
- [LLM Wallet MCP Repository](https://github.com/x402/llm-wallet-mcp) <br>
- [x402 Protocol Overview](references/x402-protocol.md) <br>
- [LLM Wallet Setup Guide](references/wallet-setup.md) <br>
- [LLM Wallet Usage Examples](references/examples.md) <br>
- [x402 Protocol Documentation](https://docs.cdp.coinbase.com/x402/welcome) <br>
- [x402 Protocol GitHub](https://github.com/coinbase/x402) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include wallet addresses, balances, transaction confirmations, payment checks, and setup guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
