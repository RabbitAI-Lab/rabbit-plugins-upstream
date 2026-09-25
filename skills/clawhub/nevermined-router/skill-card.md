## Description:

Guides agents through discovering and paying x402 or MPP services with the Nevermined Router under a capped spending delegation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agents use this skill to discover paid services, set up a spending delegation and funded wallet, make paid requests, and reconcile charges. A human controls the initial key and spending limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can spend real funds through paid service calls.

Mitigation: Install only when spending is intended; use the smallest practical delegation cap and expiry and set per-call ceilings where possible.

Risk: An agent could pay an unintended service or use the wrong network.

Mitigation: Verify the service and network before paying, and prefer the sandbox for testing.

Risk: Repeated attempts after a spending refusal could exceed human intent.

Mitigation: Do not let an agent raise budgets or create new delegations to bypass a refusal without human approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined API key portal](https://nevermined.app)
- [Service discovery guide](references/discovery.md)
- [Delegation and wallet setup](references/bootstrap.md)
- [Paying through the Router](references/paying.md)
- [Payment ledger and reconciliation](references/ledger.md)
- [Router errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HTTP and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid API requests and payment-ledger reconciliation.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata; embedded skill frontmatter says 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
