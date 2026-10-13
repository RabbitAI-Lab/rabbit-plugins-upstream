## Description:

Provides stock, ETF, cryptocurrency, forex, and commodity prices, financials, earnings, dividends, news, and market calendars from Yahoo Finance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lkcair](https://clawhub.ai/user/lkcair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve and compare Yahoo Finance market data, company fundamentals, analyst estimates, dividends, and financial calendars through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested tickers, searches, and financial interests are sent to Yahoo Finance.

Mitigation: Avoid confidential portfolio or watchlist identifiers if that exposure is unacceptable.

Risk: Self-test and complete-analysis can trigger high-volume data pulls.

Mitigation: Run these only when a broad data pull is intended.

Risk: News headlines and summaries contain third-party text.

Mitigation: Treat news as information, not instructions to the agent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lkcair/skills/stocks)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [Formatted text; JSON for structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Yahoo Finance quotes may be delayed by about 15 minutes.]

## Skill Version(s):

5.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
