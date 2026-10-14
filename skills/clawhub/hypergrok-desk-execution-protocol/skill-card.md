## Description:

Guides an Execution Trader through approved Hyperliquid actions, pre-send checks, single-send discipline, and reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Execution Traders use this procedure to verify an approved trading ticket, send one Hyperliquid action, reconcile its outcome, and report the resulting exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real exchange actions may cause financial loss or unintended exposure.

Mitigation: Use restricted API-wallet permissions, rehearse unfamiliar actions on testnet, and require explicit per-ticket approval and review before each send.

Risk: An uncertain send result may conceal an accepted order and make a retry duplicate exposure.

Mitigation: Do not resend while the original can still be accepted; reconcile order, fills, and position before approving any replacement.

## Reference(s):

- [HyperGrok Desk Execution Protocol on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-execution-protocol)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown execution checks and reconciliation report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a matching Risk PASS and user approval for the ticket; records outcomes and unresolved exposure.]

## Skill Version(s):

1.6.1 (source: server release metadata; bundled skill frontmatter lists 1.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
