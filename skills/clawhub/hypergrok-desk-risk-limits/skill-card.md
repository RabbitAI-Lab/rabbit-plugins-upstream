## Description:

Helps a trading desk set risk limits, size proposed Hyperliquid trades against live account and market conditions, and issue documented PASS or REJECT decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and desk operators use the skill to record user-approved limits, check account exposure and order-book conditions, size proposed trades, and review reasons for approving or rejecting each ticket. It also helps them inspect open positions, margin, and protective stops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads sensitive live account state and writes local desk records.

Mitigation: Install only for a trusted trading workflow and control access to the account and local records.

Risk: Trading authority could increase exposure or allow protective orders under standing approval.

Mitigation: Require explicit per-ticket approval for exposure-increasing trades; review limits and any reduce-only standing approval carefully.

Risk: Stale account data or a stop filling beyond its assumed slippage can lead to losses above the planned budget.

Mitigation: Reject missing or stale inputs, recheck the book and exposure before approval, and use conservative stop-fill assumptions.

## Reference(s):

- [HyperGrok Desk Risk Limits on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-risk-limits)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Configuration instructions]

**Output Format:** [Markdown risk limits, book checks, and PASS or REJECT trade assessments with proposed ticket fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sizing assumptions, live-data timestamps, risk gates, and reasons for rejection.]

## Skill Version(s):

1.5.0 (source: server-resolved ClawHub release; bundled skill metadata says 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
