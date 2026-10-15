## Description:

Guides agents through discovering, pricing, and paying for external x402 or MPP services with a capped Nevermined Delegation, then checking the payment ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and autonomous agents use this skill to buy individual calls from x402 or MPP services without a direct merchant account, subject to an operator-approved spending cap.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests may exhaust an approved budget or wallet balance.

Mitigation: Start in sandbox where possible, keep Delegation caps and expiries small, quote before paying, and stop on budget or funding refusals rather than creating a larger Delegation.

Risk: Repeated or ambiguous payment requests may create duplicate charges.

Mitigation: Reuse the same request ID for a purchase, retry only documented retryable errors, and reconcile uncertain outcomes in the payment ledger.

Risk: An agent may pay an unintended external merchant.

Mitigation: Use recipient allowlists when the merchant is known, check the fee-inclusive quote, and monitor ledger entries.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [API key setup and Delegation funding](references/bootstrap.md)
- [Service discovery](references/discovery.md)
- [Quoting and paying](references/paying.md)
- [Payment ledger](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Nevermined API key and a funded, capped Delegation for paid requests.]

## Skill Version(s):

0.1.36 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
