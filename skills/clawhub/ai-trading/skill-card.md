## Description:

Research US stocks and ETFs like a buy-side analyst: live quotes, technicals, fundamentals, sector context, backtests and a written trade plan with position sizing and hard risk rules. Human approval is required before any order - analysis and education, never financial advice or auto-trading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to research US-listed stocks and ETFs, review market and company data, run basic historical analyses, and prepare written trade plans with position sizing and risk checks for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calculation errors may make reported market figures or risk checks inaccurate.

Mitigation: Independently verify the reported 52-week range and recalculate overnight position sizes before relying on results.

Risk: Market-data provider fetching currently needs a code fix, and advertised risk rules may not all be enforced.

Mitigation: Use only market-data keys and user-selected CSV files; independently check figures and risk limits, and keep all decisions and order entry under human control.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rapidworker1/skills/ai-trading)
- [Data sources](artifact/references/data-sources.md)
- [Risk playbook](artifact/references/risk-playbook.md)
- [US market calendar](artifact/references/us-market-calendar.md)
- [NYSE hours and calendars](https://www.nyse.com/markets/hours-calendars)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Research summaries, market snapshots, backtest results, risk calculations, and trade plans in text, Markdown, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs require independent verification; trade plans are for human review and do not place orders.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
