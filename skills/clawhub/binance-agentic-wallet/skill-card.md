## Description:

The Binance Agentic Wallet skill helps an agent use the `baw` CLI for Binance Web3 wallet sign-in, balance and history queries, token transfers, DEX swaps, limit orders, prediction markets, x402 payments, approvals, external signing, and DeFi operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binance-skills-hub](https://clawhub.ai/user/binance-skills-hub)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent prepare and run Binance Agentic Wallet CLI workflows for wallet operations, trading, token approvals, external signing, and DeFi actions. It is intended for assisted wallet operation where users review and confirm sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help operate a Binance Agentic Wallet, including transfers, trades, approvals, external signing, x402 payments, and DeFi actions.

Mitigation: Install it only for intended wallet operation, approve the npm CLI install intentionally, and verify each recipient, token, chain, amount, order, approval, and x402 payment before confirming.

Risk: Unattended trading or signing could lead to irreversible transactions or unintended market exposure.

Mitigation: Avoid unattended trading or signing, preserve explicit confirmation for state-changing actions, and use preview or pre-check flows before trading, DeFi, external signing, and x402 payment execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binance-skills-hub/skills/binance-agentic-wallet)
- [Authentication](references/authentication.md)
- [Preflight Checks](references/preflight.md)
- [Wallet View Commands](references/wallet-view.md)
- [Wallet Settings](references/wallet-setting.md)
- [Send Tokens](references/send.md)
- [Market Order](references/market-order.md)
- [Limit Order](references/limit-order.md)
- [Token Approvals](references/approvals.md)
- [External Sign](references/external-sign.md)
- [Prediction Markets](references/prediction.md)
- [x402 Payment](references/x402-payment.md)
- [DeFi Commands](references/defi.md)
- [Security Reference](references/security.md)
- [Speed Up & Cancel Pending Transactions](references/speedup-cancel.md)
- [bStock AI Trading Competition Campaign Reference](references/campaign.md)
- [bStock eligible tokens developer docs](https://web3.binance.com/en/dev-docs/products/agentic-wallet/use-cases/campaigns/bstock-eligible-tokens)
- [bStock PnL contest developer docs](https://web3.binance.com/en/dev-docs/products/agentic-wallet/use-cases/campaigns/bstock-pnl-contest)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON-oriented command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are expected to use machine-readable JSON output and require user confirmation for state-changing wallet actions.]

## Skill Version(s):

1.9.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
