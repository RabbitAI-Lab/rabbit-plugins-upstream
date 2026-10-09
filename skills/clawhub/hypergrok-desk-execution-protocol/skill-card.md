## Description:

Guides a trading desk agent through approval checks, single-action Hyperliquid execution, uncertain-result recovery, and post-trade reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading desk operators use this skill to turn an approved ticket into one Hyperliquid order or account action, then reconcile its outcome and report it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trading actions can create or change financial exposure without the intended authorization.

Mitigation: Require a matching Risk PASS, ticket-specific user approval, and verified approval gates for every send, cancel, modify, leverage change, or close.

Risk: Untrusted credentials or wallet configuration can expose the main wallet or target the wrong account.

Mitigation: Confirm the referenced trading skills and wallet setup are trusted, use an API wallet rather than a main wallet, and verify the account and network before acting.

Risk: An uncertain response can lead to a duplicate trade if the original action still succeeds.

Mitigation: Do not retry an unknown send; reconcile orders, fills, and positions, and require expiry plus fresh approval before replacing it.

## Reference(s):

- [HyperGrok Desk Execution Protocol on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-execution-protocol)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown execution checklist and reconciliation report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One approved action per ticket; records send status, fills, exposure, and next steps.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
