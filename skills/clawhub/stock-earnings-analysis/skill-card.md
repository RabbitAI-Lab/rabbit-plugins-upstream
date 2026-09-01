## Description:

Earnings analysis for US stocks, organized the way a quarter actually reads: the per-quarter analysis report of what a company reported, with the editorial headline, marquee KPI highlights and their year-over-year deltas, the guidance language as management phrased it, and a summary of the earnings call, plus SEC risk-factor diffs attached to the quarter they belong to, the AI takeaway signal, who reported in the last week, and the forward calendar of who reports next. Every claim carries its fiscal period and report date, and absence is stated rather than skipped. Use for "analyze AAPL earnings", "earnings report analysis", "earnings call summary", "who reported earnings this week", "post earnings review", "upcoming earnings preview". Read-only. No trading, no purchases, no write operations, no wallet access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build read-only US stock earnings readouts that organize reported results, call summaries, guidance, SEC risk-factor changes, earnings signals, recent reporters and upcoming earnings calendars by fiscal quarter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a SentiSense API key to the SentiSense service for financial data requests.

Mitigation: Use a dedicated read-only SentiSense API key and avoid sharing keys beyond the configured API calls.

Risk: Financial earnings summaries and signals can be mistaken for trading recommendations.

Mitigation: Present outputs as research and education only, preserve the not-investment-advice disclaimer, and do not place trades or modify accounts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown earnings analysis with cited fiscal periods, report dates and stated data absences]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only financial research output; not investment advice and not a trading or account-management action.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
