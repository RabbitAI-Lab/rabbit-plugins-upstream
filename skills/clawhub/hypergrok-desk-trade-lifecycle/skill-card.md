## Description:

Guides a HyperGrok desk trade from proposal and market evidence through risk sign-off, explicit user approval, execution, reconciliation, and review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk users and their agents use this skill to document and control position openings, adjustments, and closures through fresh market evidence, risk checks, explicit approval, and post-trade review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exchange actions can cause financial loss or unintended live trades.

Mitigation: Keep exchange keys and mainnet execution behind trusted approval controls; rehearse the full workflow on testnet first.

Risk: Stale market data or reused approval can invalidate a trade ticket.

Mitigation: Refresh evidence and risk sign-off for expired or changed tickets, and require the user's exact approval for each new ticket.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-trade-lifecycle)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown trade proposals, tickets, and journal entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposal IDs and UTC timestamps track each stage; every execution requires current risk sign-off and explicit user approval.]

## Skill Version(s):

1.6.1 (source: ClawHub release evidence; bundled skill metadata: 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
