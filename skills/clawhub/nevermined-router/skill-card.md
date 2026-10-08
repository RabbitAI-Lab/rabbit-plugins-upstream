## Description:

Guides agents through discovering and paying for x402 or MPP service calls with Nevermined Router under a capped spending delegation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find payable services, create a capped spending delegation, quote and route paid requests, and reconcile charges in the payment ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests can spend a user's funds or exceed their intended per-call price.

Mitigation: Start in sandbox, use small short-lived delegations, quote once per decision, enforce a fee-inclusive price ceiling, and obtain human approval before raising budgets.

Risk: Credentials or sensitive information could be exposed to an external service.

Mitigation: Do not forward the Nevermined API key or include secrets in routed request bodies or forwarded headers; prefer catalog slugs over raw URLs.

Risk: Retrying an uncertain paid call with a new request ID could charge twice.

Mitigation: Reuse one request ID per purchase and check the payment result or ledger instead of starting a new payment.

Risk: An agent could accept legal terms without the account holder's consent.

Mitigation: Require human approval before accepting legal terms.

## Reference(s):

- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined API keys](https://nevermined.app)
- [Bootstrap and spending delegations](references/bootstrap.md)
- [Service discovery](references/discovery.md)
- [Paying and quoting](references/paying.md)
- [Errors and guardrails](references/errors.md)
- [Payment ledger](references/ledger.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HTTP and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.30 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
