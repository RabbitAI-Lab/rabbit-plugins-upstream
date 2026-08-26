## Description:

Bitcoin Lightning wallet for agents - balances, invoices, payments, BTC/USD swaps, QR codes, price conversion, transaction history, and L402 auto-pay client via the Blink API. All output is JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pretyflaco](https://clawhub.ai/user/pretyflaco)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to operate Blink Bitcoin Lightning wallets: checking balances, creating invoices, sending payments, converting between BTC and USD wallets, tracking transactions, and accessing L402-gated services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute live wallet operations, including spending funds through Write-scoped Blink API keys.

Mitigation: Use staging first, prefer read/receive-only API keys, add Write scope only when needed, check balances and fees before payment, and require explicit user confirmation for payment amount and recipient.

Risk: Non-custodial Spark operations can use SPARK_MNEMONIC, which grants spend authority over the account.

Mitigation: Avoid giving SPARK_MNEMONIC to shared agents, keep it environment-only, never log or display it, and clear local Spark state when it is no longer needed.

Risk: L402 auto-pay can spend sats and may reuse cached paid tokens silently.

Mitigation: Configure explicit hourly and daily budgets plus a non-empty domain allowlist before auto-pay, dry-run first, confirm the satoshi amount, and clear ~/.blink token and root-key state when no longer needed.

Risk: The skill persists local operational state such as L402 tokens, budget files, spending logs, and temporary QR PNGs.

Mitigation: Use the provided clear/reset options for token and budget state, disable L402 token storage with --no-store when appropriate, and remove temporary QR files after use.

## Reference(s):

- [Blink API and Auth](references/blink-api-and-auth.md)
- [Payment Operations](references/payment-operations.md)
- [Invoice Lifecycle](references/invoice-lifecycle.md)
- [Swap Operations](references/swap-operations.md)
- [Non-Custodial Spark Accounts](references/non-custodial.md)
- [Homepage](https://github.com/blinkbitcoin/blink-skill)
- [Blink Agent Playbook](https://dev.blink.sv/api/agent-playbook)
- [Blink AI Metadata](https://dev.blink.sv/llms.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON command output with Markdown instructions and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet scripts produce structured JSON; QR generation can also create temporary PNG files.]

## Skill Version(s):

1.8.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
