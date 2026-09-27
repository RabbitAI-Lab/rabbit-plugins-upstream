## Description:

Guides agents through discovering, pricing, and buying per-request services through the Nevermined Router within a delegated spending budget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agents use this skill to discover x402 or MPP services, quote prices before paying, make budget-limited paid calls, and reconcile spending through Nevermined's ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous purchases can spend funds beyond the user's intended amount.

Mitigation: Start in the sandbox or use a small Delegation with a short expiry, quote calls first, and set a per-call maxTotalCents limit.

Risk: Repeating a paid request may result in another charge.

Mitigation: Use stable requestIds and inspect the payment ledger before retrying uncertain outcomes.

Risk: Routed requests can disclose private information or credentials to an external merchant.

Mitigation: Only route data to trusted merchants; keep the Nevermined API key out of merchant requests and avoid sending secrets or private data in request bodies.

## Reference(s):

- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined Agent Services Catalog](https://nevermined.app/catalog/ai-catalog.json)
- [Nevermined API keys](https://nevermined.app)
- [ClawHub skill release](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Bootstrap and delegation guidance](references/bootstrap.md)
- [Service discovery guidance](references/discovery.md)
- [Payment and routing guidance](references/paying.md)
- [Error and guardrail guidance](references/errors.md)
- [Payment ledger guidance](references/ledger.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HTTP request examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for quoting, routing paid requests, and reviewing payment records.]

## Skill Version(s):

0.1.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
