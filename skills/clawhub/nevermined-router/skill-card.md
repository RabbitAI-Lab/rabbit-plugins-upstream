## Description:

Guides an AI agent through discovering external x402 or MPP services, setting a capped spending Delegation, quoting and paying for calls through the Nevermined Router, and reviewing the payment ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to make controlled, per-request purchases from x402 or MPP services without separate accounts with those services. It explains service discovery, spending limits, quotes, payment calls, and ledger review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Router calls spend funds from the buyer wallet, subject to the Delegation's spending limit.

Mitigation: Set and review a spending cap before use, quote each call before paying, and check the ledger after purchases.

Risk: The security review notes a payment-settlement action beyond the stated routing and ledger-reading purpose, and says some references were unresolved.

Mitigation: Review the settlement-related guidance and unresolved references before installation; do not treat the benign verdict as a safety guarantee.

## Reference(s):

- [Nevermined Router overview](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined service catalog](https://nevermined.app/catalog/ai-catalog.json)
- [Router buyer identity](https://nevermined.ai/docs/products/catalog/router/buyer-identity)
- [Service discovery reference](references/discovery.md)
- [Delegation setup reference](references/bootstrap.md)
- [Payment and safety errors reference](references/errors.md)
- [Payment ledger reference](references/ledger.md)
- [Paying for services reference](references/paying.md)
- [ClawHub release](https://clawhub.ai/nevermined-io/skills/nevermined-router)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes payment guardrails, quote-before-pay guidance, and ledger reconciliation steps.]

## Skill Version(s):

0.1.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
