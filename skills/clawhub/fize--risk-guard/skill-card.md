## Description:

Risk Guard is a Chinese-language pre-trade risk-control skill that checks quantitative signal consistency, estimates position and stop-loss limits, and can veto trades when data or risk gates fail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, research analysts, and trading-assistant agents use this skill before buy decisions to cross-check technical signals, calibrate position limits, set dynamic stop-loss levels, and identify conditions that should block a trade.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could mistake position limits, stop-loss levels, or veto outcomes for financial advice or automatic trading authorization.

Mitigation: Treat reports as decision support only and require independent review before any trade.

Risk: Risk reports can be unreliable if required market breadth, limit-up/down, moving-average, or MACD data are unavailable or stale.

Mitigation: Verify market data through authoritative sources and block the assessment when required data cannot be obtained.

## Reference(s):

- [ClawHub skill page: risk-guard](https://clawhub.ai/fize/skills/risk-guard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown risk-control audit report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language decision-support report with signal checks, position limits, stop-loss guidance, risk level, and veto outcome.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
