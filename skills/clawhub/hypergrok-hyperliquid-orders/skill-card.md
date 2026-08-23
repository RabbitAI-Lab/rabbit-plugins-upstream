## Description:

Place, cancel and modify Hyperliquid orders correctly from the desk computer - limit and IOC (market-style) orders, take-profit and stop-loss trigger orders with grouping, client order ids, reduce-only, batch actions, price and size rounding, and how to read every response status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Execution traders and trading-desk agents use this skill to prepare, execute, cancel, modify, and reconcile approved Hyperliquid order actions by client order id. It is intended for workflows with an approved ticket, risk pass, and explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a Hyperliquid API wallet key that can authorize real orders when configured for mainnet.

Mitigation: Install only in an approved trading workflow, keep the API wallet tightly scoped, protect key material, and rehearse on testnet before using mainnet.

Risk: Order instructions could place, cancel, or modify positions incorrectly if used outside the stated approval flow.

Mitigation: Require an approved ticket, Risk PASS, explicit user approval, and reconciliation by client order id for order actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-orders)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Python, TypeScript, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes order-action examples, response interpretation guidance, and operational safety checks.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
