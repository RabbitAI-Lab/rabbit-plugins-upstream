## Description:

The end-to-end procedure for one trade on the HyperGrok desk - from an idea to a reviewed, journaled result - with the ticket format, ownership at each stage, and explicit completion criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-desk operators use this skill to run a consistent lifecycle for opening, adjusting, closing, reconciling, and reviewing HyperGrok desk positions. It helps agents structure proposals, risk sign-off, exact approval phrases, execution notes, and post-trade records before any exchange write path is used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial actions could occur without adequate review or consent.

Mitigation: Require a complete ticket, risk sign-off, and the exact approval phrase for the proposal id before any exchange write path is used.

Risk: Market data, account state, or ticket parameters may become stale before execution.

Mitigation: Refresh evidence and risk sign-off when a ticket expires or when prices, book depth, or account state have changed.

Risk: Operational records may diverge from actual exchange state.

Mitigation: Record execution responses, reconcile against exchange records, and journal the final review in the proposal file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-trade-lifecycle)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown procedure guidance with ticket and proposal templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces structured trading-desk workflow guidance and records; no exchange action is authorized without the required ticket and exact approval phrase.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
