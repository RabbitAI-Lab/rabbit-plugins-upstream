## Description:

Guides authorized desk traders through placing, canceling, modifying, and reconciling Hyperliquid orders, including limit, IOC, and take-profit or stop-loss orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Authorized Execution Traders use this skill to prepare and execute Hyperliquid order actions on an approved desk ticket, then reconcile order statuses and client order IDs. Risk approval and explicit user approval are required before signed actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed orders on mainnet can cause real financial loss.

Mitigation: Restrict use to authorized accounts and the Execution Trader; require a ticket, Risk PASS, and explicit user approval before each order action.

Risk: Exposure from a compromised or overprivileged API wallet.

Mitigation: Protect the private key and limit wallet permissions and funding.

Risk: An uncertain order response could lead to duplicate execution.

Mitigation: Reconcile by client order ID before retrying a signed action.

## Reference(s):

- [HyperGrok Hyperliquid Orders on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-orders)

## Skill Output:

**Output Type(s):** [Guidance, Code]

**Output Format:** [Markdown with Python, TypeScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes order-status interpretation and reconciliation guidance.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata; bundled skill frontmatter says 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
