## Description:

Bitcoin Lightning wallet for agents for balances, invoices, payments, BTC/USD swaps, QR codes, price conversion, transaction history, and L402 auto-pay via the Blink API, with JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pretyflaco](https://clawhub.ai/user/pretyflaco)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to perform concrete Blink wallet operations, including checking balances, receiving invoices, sending Lightning payments, converting between BTC and USD wallets, and using L402-gated services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform real Bitcoin wallet operations, including irreversible payments and swaps.

Mitigation: Use read/receive-only API keys unless spending is required, test on staging for trials, check balance and fees before payment, and require explicit user confirmation before send, swap, Spark send, or L402 pay operations.

Risk: Self-custodial Spark use can grant spend authority to the agent process through SPARK_MNEMONIC.

Mitigation: Do not provide SPARK_MNEMONIC unless self-custodial signing is intended; keep seeds in environment variables only and avoid logging, displaying, transmitting, or storing them.

Risk: L402 auto-pay, producer keys, third-party discovery, and stored bearer payment tokens can create ongoing spend or access exposure.

Mitigation: Configure L402 budgets and domain allowlists before auto-pay, dry-run and confirm payment amounts, use --no-store when token persistence is not needed, and clear ~/.blink token or key state when finished.

## Reference(s):

- [Blink API And Auth](references/blink-api-and-auth.md)
- [Invoice Lifecycle](references/invoice-lifecycle.md)
- [Non-Custodial (Spark) Accounts](references/non-custodial.md)
- [Payment Operations](references/payment-operations.md)
- [Swap Operations](references/swap-operations.md)
- [Blink Skill Repository](https://github.com/blinkbitcoin/blink-skill)
- [Blink API Docs](https://dev.blink.sv)
- [ClawHub Skill Page](https://clawhub.ai/pretyflaco/skills/blink)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Structured JSON to stdout, status and errors to stderr, and optional PNG files for invoice QR codes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated wallet operations require Node.js and BLINK_API_KEY; subscriptions may require modern Node WebSocket support; L402 and budget flows may persist state under ~/.blink.]

## Skill Version(s):

1.7.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
