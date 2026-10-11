## Description:

Guides approved Hyperliquid order placement, modification, cancellation, and reconciliation, including limit, IOC, and protective trigger orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Authorized execution traders use this skill to prepare and execute Hyperliquid orders against risk-approved tickets, then reconcile order outcomes by client order ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order actions can move funds or change positions without the intended authorization.

Mitigation: Require a risk-approved ticket and fresh, explicit user approval for every order action; use a limited API wallet and protect its private key.

Risk: Unexpected live trading or prices outside the approved slippage bound.

Mitigation: Keep testnet as the default until rehearsed and check final encoded prices against the approved ticket before signing.

Risk: A lost response or partial fill can cause duplicate orders or leave a position without protection.

Mitigation: Reconcile uncertain results by client order ID before retrying; check partial fills and place a standalone stop for any unprotected filled size.

## Reference(s):

- [HyperGrok Hyperliquid Orders on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-orders)

## Skill Output:

**Output Type(s):** [Code, Guidance]

**Output Format:** [Markdown with Python and TypeScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes order-status interpretation and client order ID reconciliation guidance.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata; bundled skill frontmatter lists 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
