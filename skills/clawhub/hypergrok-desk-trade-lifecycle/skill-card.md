## Description:

Guides a HyperGrok trading desk through a trade from proposal and risk review to user approval, execution, reconciliation, and journaled review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading desk operators and agents use this workflow to document, approve, execute, reconcile, and review position changes on testnet or mainnet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overly broad preauthorization could allow high-impact trading actions without a fresh prompt.

Mitigation: Keep desk preauthorizations narrow and require explicit, ticket-specific user approval for other actions.

Risk: An exchange write route could bypass the intended approval gate.

Mitigation: Verify that the native approval gate covers the actual write route before enabling execution; otherwise remain research-only.

## Reference(s):

- [HyperGrok Desk Trade Lifecycle on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-trade-lifecycle)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown trade proposals, tickets, execution reports, and reviews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tickets include risk sign-off, an explicit user approval phrase, expiry, and reconciliation records.]

## Skill Version(s):

1.5.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
