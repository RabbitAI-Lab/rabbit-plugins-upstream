## Description:

Guides a Hyperliquid trading desk through incident containment, exchange-state reconciliation, approved corrective actions, and review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk operators and their agents use this skill to respond to mismatched orders or positions, unprotected exposure, exchange outages, and suspected API-wallet compromise while preserving approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect or duplicate trading actions can increase exposure after an uncertain send or unexpected fill.

Mitigation: Pause new risk, reconcile against exchange records, and require a fresh ticket, risk check, and user approval before corrective orders.

Risk: An unprotected position or exchange outage can leave exposure unmanaged.

Mitigation: Prioritize protective stops using verified live state and approved tickets; pause new risk until account state and protection are reconciled.

Risk: A compromised API wallet may allow unauthorized trading.

Mitigation: Have the user revoke the wallet immediately, assess exchange activity, and rotate credentials through the secure secret store.

## Reference(s):

- [HyperGrok Desk Incident Response on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-incident-response)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown incident notices, tickets, reconciliation guidance, and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Corrective exchange actions require approved tickets and risk checks.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata; artifact frontmatter lists 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
