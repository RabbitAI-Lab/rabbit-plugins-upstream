## Description:

SentiSense gives AI agents read-only access to U.S. stock market data, including sentiment, SentiSense Scores, insider and congressional trades, 13F institutional flows, options positioning, analyst ratings, earnings calendars, AI-generated insights, and delayed stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market-research agents use this skill to query SentiSense's read-only financial data API for stock sentiment, market data, filings, options, analyst, earnings, and AI insight workflows. Outputs are informational and are not investment advice or trade execution instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial outputs may be mistaken for investment advice or live trading signals.

Mitigation: Present results as informational research, keep the not-investment-advice caveat visible, and do not use the skill for trading, purchases, or order execution.

Risk: The account-personalized insights endpoint can reflect an authenticated user's watchlist or portfolio.

Mitigation: Use public stock and market endpoints for generic research, and call /api/v1/insights/user only when the user intentionally wants account-personalized insights.

Risk: Stock prices can be delayed or stale, especially outside regular trading hours or for delisted symbols.

Mitigation: Label quotes as delayed, use priceAsOf when available, treat missing freshness as unknown age, and avoid decisions that require live market ticks.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense website](https://sentisense.ai)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [Latest SentiSense skill file](https://sentisense.ai/skill.md)

## Skill Output:

**Output Type(s):** [API Calls, Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with REST API examples, JSON response descriptions, and shell or code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for authenticated endpoints; several data surfaces are free-tier, preview, quota-gated, or PRO-only.]

## Skill Version(s):

2.11.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
