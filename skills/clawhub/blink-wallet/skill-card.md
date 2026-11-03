## Description:

Bitcoin Lightning wallet for agents — balances, invoices, payments, BTC/USD swaps, QR codes, price conversion, transaction history, non-custodial (Spark) accounts, and L402 auto-pay client via the Blink API. All output is JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pretyflaco](https://clawhub.ai/user/pretyflaco)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Blink to check wallet balances, create and monitor Lightning invoices, send payments, convert between BTC and USD, and interact with L402 services. The skill also supports non-custodial Spark wallet operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The payment verifier may accept a token without enforcing which resource it unlocks.

Mitigation: Verify payment proofs against the actual requested resource and reject requests when that context is missing.

Risk: Wallet credentials, seeds, and local wallet or payment state are sensitive.

Mitigation: Protect local wallet files, keep credentials and seeds out of logs, and isolate requests involving untrusted URLs.

Risk: The external Spark SDK is outside the stated security review, and missing payment proofs can leave payments unusable.

Mitigation: Use test funds or regtest while evaluating Spark operations, and verify payment proofs before relying on paid access.

## Reference(s):

- [Blink API and authentication](references/blink-api-and-auth.md)
- [Payment operations](references/payment-operations.md)
- [Invoice lifecycle](references/invoice-lifecycle.md)
- [Swap operations](references/swap-operations.md)
- [Non-custodial Spark operations](references/non-custodial.md)
- [Blink Agent Playbook](https://dev.blink.sv/api/agent-playbook)
- [Blink agent discovery metadata](https://dev.blink.sv/llms.txt)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON command results, with optional QR invoice PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured wallet, invoice, payment, transaction, price, and swap results; QR image output is optional.]

## Skill Version(s):

3.0.1 (source: SKILL.md frontmatter and server-resolved release version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
