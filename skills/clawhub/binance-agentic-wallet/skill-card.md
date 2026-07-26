## Description: <br>
This skill guides an agent in using the `baw` CLI to manage a Binance Web3 wallet, including authentication, balances, transfers, swaps, limit orders, prediction markets, x402 payments, approvals, and DeFi operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binance-skills-hub](https://clawhub.ai/user/binance-skills-hub) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to route wallet-related requests into reviewed `baw` CLI commands and readable summaries. It supports wallet setup, token transfers, trading, approvals management, prediction-market actions, x402 payments, and DeFi position or transaction workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect real wallet funds through transfers, trades, approvals, prediction-market actions, x402 payments, and DeFi transactions. <br>
Mitigation: Before any state-changing action, require the user to review the exact command, recipient, chain, token address, amount, order IDs, fees, and whether the action can execute later or be irreversible. <br>
Risk: The skill instructs the agent to install or upgrade the global `@binance/agentic-wallet` npm package. <br>
Mitigation: Install or upgrade only after the user trusts the package and publisher and has approved the global npm change. <br>
Risk: Market, limit-order, payment, and DeFi actions can fail, remain pending, or rely on stale backend data after submission. <br>
Mitigation: Represent transaction hashes as submission evidence only, avoid claiming completion before confirmation, and use the documented preview, security-check, and verification flows. <br>


## Reference(s): <br>
- [ClawHub Release Page](https://clawhub.ai/binance-skills-hub/skills/binance-agentic-wallet) <br>
- [Authentication](references/authentication.md) <br>
- [Preflight Checks](references/preflight.md) <br>
- [Security Reference](references/security.md) <br>
- [Wallet View Commands](references/wallet-view.md) <br>
- [Wallet Settings](references/wallet-setting.md) <br>
- [Send Tokens](references/send.md) <br>
- [Market Orders](references/market-order.md) <br>
- [Limit Orders](references/limit-order.md) <br>
- [Token Approvals](references/approvals.md) <br>
- [Prediction Commands](references/prediction.md) <br>
- [x402 Payment](references/x402-payment.md) <br>
- [DeFi Commands](references/defi.md) <br>
- [Binance Web3 Wallet Trading Fees](https://www.binance.com/en/support/faq/detail/87cbb1ca0df34a348eaecb73c26167d7) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [State-changing wallet operations require explicit user confirmation; CLI commands are expected to include `--json`.] <br>

## Skill Version(s): <br>
1.4.0 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
