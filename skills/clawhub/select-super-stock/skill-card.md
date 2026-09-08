## Description:

A single-symbol A-share technical research helper that verifies completed daily trading data, computes basic trend indicators, and reports data gaps without screening stocks or giving trading advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[georgetao730](https://clawhub.ai/user/georgetao730)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect one explicitly supplied six-digit A-share symbol against completed daily OHLCV data, moving averages, RSI14, and 52-week range context. It is intended for learning and informational research, not portfolio construction, ranking, price targets, or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delayed public daily-bar data may be mistaken for real-time market data or investment advice.

Mitigation: Keep the report labels for trade date, collection time, source, adjustment method, non-real-time status, and learning-only disclaimer visible in downstream use.

Risk: Unavailable, incomplete, stale, or malformed market data could otherwise lead to unsupported conclusions.

Mitigation: Use the skill's unavailable status and missing-field behavior as a hard stop for market conclusions, and verify important financial decisions against independent dated sources.

Risk: Users may overextend a single-stock technical observation into screening, ranking, portfolio sizing, or trade execution.

Mitigation: Limit use to one user-specified A-share symbol and avoid asking the skill for stock selection, scores, target prices, position sizing, order placement, or account actions.

## Reference(s):

- [Data and Research Boundaries](artifact/references/data-policy.md)
- [Risk Boundaries](artifact/references/risk-boundary.md)
- [ClawHub Skill Page](https://clawhub.ai/georgetao730/skills/select-super-stock)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text research report or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports source, trade date, collection time, adjustment method, non-real-time daily-bar status, missing coverage, and a learning-only disclaimer.]

## Skill Version(s):

1.4.0 (source: server release metadata and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
