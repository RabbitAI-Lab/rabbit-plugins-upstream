## Description:

Bitcoin Lightning wallet for agents: balances, invoices, payments, BTC/USD swaps, QR codes, price conversion, transaction history, non-custodial Spark accounts, and L402 auto-pay via the Blink API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pretyflaco](https://clawhub.ai/user/pretyflaco)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to operate Blink Lightning wallets, receive and send payments, inspect balances and transaction history, run BTC/USD swaps, and access L402-gated services with explicit budget controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Lightning wallet funds.

Mitigation: Use read- or receive-only API keys unless sending is required, confirm recipient and amount before payment, probe fees, check balances, and prefer staging for tests.

Risk: L402 payment tokens and spending logs may persist locally and reusable tokens can avoid a new payment prompt.

Mitigation: Configure small L402 budgets, use a tight domain allowlist, choose --no-store when cached tokens are not needed, and review local state under ~/.blink.

Risk: Security evidence reports a DNS-based internal-network bypass in the URL guard.

Mitigation: Avoid probing or paying untrusted URLs and restrict L402 use to known domains through the allowlist.

Risk: SPARK_MNEMONIC grants spend authority for non-custodial Spark operations.

Mitigation: Expose SPARK_MNEMONIC only for deliberate Spark workflows and never log, display, or store the mnemonic.

## Reference(s):

- [Blink ClawHub Skill](https://clawhub.ai/pretyflaco/skills/blink-wallet)
- [Publisher Profile](https://clawhub.ai/user/pretyflaco)
- [Blink Skill Homepage](https://github.com/blinkbitcoin/blink-skills)
- [Blink API And Auth](references/blink-api-and-auth.md)
- [Invoice Lifecycle](references/invoice-lifecycle.md)
- [Payment Operations](references/payment-operations.md)
- [Swap Operations](references/swap-operations.md)
- [Non-Custodial (Spark) Accounts](references/non-custodial.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [JSON command output with Markdown guidance and optional QR PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may require wallet credentials, outbound network access, and local wallet or token state under ~/.blink.]

## Skill Version(s):

2.6.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
