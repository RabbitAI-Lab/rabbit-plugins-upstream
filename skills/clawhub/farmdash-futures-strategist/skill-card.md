## Description:

Hyperliquid perps strategist: market scans, funding rates, position sizing, and user-signed EIP-712 order execution & cancellation with drawdown guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and agent developers use this skill to research Hyperliquid perpetual futures, compare strategies, size positions, and prepare, sign, execute, or cancel orders under the selected execution mode and risk controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opt-in bounded autonomous trading may place or cancel orders without per-order confirmation when its delegation conditions are met.

Mitigation: Choose the execution mode explicitly; review the owner-signed policy bounds and live readiness, or use USER_SIGNED for fresh approval on each action.

Risk: Perpetual futures can cause financial losses, and an unclear venue submission can leave order status uncertain.

Mitigation: Use the stated sizing and drawdown guardrails, check current account and market information, and reconcile with the venue before retrying an ambiguous order.

Risk: Using the skill sends requests to FarmDash and Hyperliquid services.

Mitigation: Review the skill's data disclosure and request behavior before use, and proceed only if those external requests are acceptable.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash Futures Strategist Skill Manual](https://www.farmdash.one/openclaw-skills/farmdash-futures-strategist/SKILL.md)
- [FarmDash API Schema](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash Security and Authority Boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [Analysis, JSON, API Calls, Guidance]

**Output Format:** [Structured market and strategy analysis, API request and response data, and user-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution depends on current market and account data, venue authority, the selected execution mode, and its required signatures and checks.]

## Skill Version(s):

1.0.30 (source: server-resolved ClawHub release metadata; artifact frontmatter reports 3.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
