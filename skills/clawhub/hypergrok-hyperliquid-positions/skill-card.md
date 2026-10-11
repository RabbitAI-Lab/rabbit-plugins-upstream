## Description:

Helps authorized trading-desk users inspect Hyperliquid perpetual positions and margin, check protection, and manage leverage, isolated margin, and position closes under approved tickets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Authorized trading-desk staff use this skill to review Hyperliquid positions, margin tiers, liquidation prices, and protective orders. Execution Traders can use approved tickets to change leverage or isolated margin and close positions while checking the remaining protection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Leverage, margin, and close actions can materially change financial exposure.

Mitigation: Limit write actions to authorized Execution Traders with approved tickets; rehearse on testnet before mainnet use.

Risk: Closing or cleaning up orders incorrectly can leave a remaining position unprotected or retain orphaned triggers.

Mitigation: Read live position state before and after a close; preserve or replace stops for partial closes, and cancel orphaned triggers only after confirming a full close.

## Reference(s):

- [HyperGrok Hyperliquid Positions on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-positions)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell, Python, and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Position and protection checks plus ticket-gated trading instructions; actions require an authorized account.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
