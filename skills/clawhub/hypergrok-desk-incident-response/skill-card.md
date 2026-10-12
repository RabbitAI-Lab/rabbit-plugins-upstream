## Description:

Guides a Hyperliquid trading desk through incident containment, exchange-state reconciliation, approved recovery actions, and post-incident review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk operators and agents use this playbook to respond to uncertain orders, unexpected exposure, lost protection, exchange outages, and suspected API wallet compromise while preserving user approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uncertain order results or stale account state could lead to duplicate orders or unintended exposure.

Mitigation: Pause new risk, reconcile orders and fills against the exchange record, and require a new approved ticket before any replacement order.

Risk: An unprotected or oversized position may suffer further losses while the desk waits for approval.

Mitigation: Alert the user promptly with exposure details and use approved reduce-only or protective-stop tickets; escalate to the user for direct action if approval is unavailable.

Risk: A compromised API wallet or exposed trading key could permit unauthorized trades.

Mitigation: Use trade-only API wallets and a secure secret store; have the user revoke compromised credentials immediately and rotate the key after assessing exposure.

## Reference(s):

- [HyperGrok Desk Incident Response on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-incident-response)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Incident response tickets]

**Output Format:** [Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incident declarations, exchange reconciliation steps, approval-gated containment tickets, and review guidance.]

## Skill Version(s):

1.5.0 (source: server-resolved ClawHub release; bundled frontmatter says 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
