## Description:

Bitcoin Lightning wallet for agents — balances, invoices, payments, BTC/USD swaps, QR codes, price conversion, transaction history, non-custodial (Spark) accounts, and L402 auto-pay client via the Blink API. All output is JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pretyflaco](https://clawhub.ai/user/pretyflaco)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building agent workflows use Blink to inspect Lightning wallets, create and pay invoices, manage BTC/USD conversions, and access L402-protected services. It also supports self-custodial Spark wallet operations when configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-scoped credentials and a Spark seed can authorize payments that cannot be reversed after settlement.

Mitigation: Begin with Read/Receive credentials and test funds; use a dedicated low-balance wallet, review payment previews, and keep confirmations enabled.

Risk: L402 auto-pay can spend funds, while configured limits exclude routing fees and plain token spending.

Mitigation: Set small budgets and a narrow domain allowlist, and account separately for fees and token spending.

Risk: Reusable access credentials and L402 payment tokens are stored under ~/.blink.

Mitigation: Protect ~/.blink and run the skill without elevated privileges.

Risk: Optional Spark dependencies were not included in the security review, which was static.

Mitigation: Independently verify the optional Spark dependencies and their versions before using Spark commands.

## Reference(s):

- [Blink API and authentication](artifact/references/blink-api-and-auth.md)
- [Payment operations](artifact/references/payment-operations.md)
- [Invoice lifecycle](artifact/references/invoice-lifecycle.md)
- [Non-custodial Spark wallets](artifact/references/non-custodial.md)
- [Swap operations](artifact/references/swap-operations.md)
- [Blink Agent Playbook](https://dev.blink.sv/api/agent-playbook)
- [Blink machine-readable discovery metadata](https://dev.blink.sv/llms.txt)
- [ClawHub release](https://clawhub.ai/pretyflaco/skills/blink-wallet)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON command results, with optional QR-code PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured results; QR generation can write a temporary PNG file.]

## Skill Version(s):

3.0.4 (source: skill frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
