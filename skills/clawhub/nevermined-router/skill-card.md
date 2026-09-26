## Description:

Guides agents through discovering x402 or MPP services and making budget-capped paid calls through the Nevermined Router, including wallet funding, payment records, and spending guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agents use this skill to discover payable services, make individual paid requests within a human-approved budget, and reconcile spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with payment authority can incur real charges from external services.

Mitigation: Test with sandbox keys; set tight Delegation caps and expirations, and scope recipients when the merchant is known.

Risk: Sensitive request content or credentials could be sent to a merchant.

Mitigation: Review merchant credentials and request bodies before routing; never forward the Nevermined API key to a merchant.

Risk: Retries or attempts to bypass refusals can cause duplicate or unauthorized spending.

Mitigation: Reuse one request ID per purchase, retry only documented transient errors, and stop rather than widening or replacing an exhausted Delegation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined app (API keys)](https://nevermined.app)
- [Service catalog](https://nevermined.app/catalog/ai-catalog.json)
- [Bootstrap and Delegations](references/bootstrap.md)
- [Service discovery](references/discovery.md)
- [Paid requests](references/paying.md)
- [Payment ledger](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with HTTP request examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes payment checks, error handling, and reconciliation guidance.]

## Skill Version(s):

0.1.25 (source: ClawHub release metadata; bundled skill text says 0.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
