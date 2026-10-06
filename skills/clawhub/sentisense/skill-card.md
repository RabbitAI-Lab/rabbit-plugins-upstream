## Description:

Provides agents with read-only US stock-market data, sentiment, ratings, filings, institutional activity, and AI-generated insights through the SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to research US stocks, monitor market sentiment and disclosed trading activity, and summarize market data without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service can associate market-data requests, tickers, searches, watchlists, and screener filters with an API key.

Mitigation: Use an appropriately scoped account, avoid sharing sensitive research queries, and keep the API key private.

Risk: Market data and AI-generated insights can be incomplete, delayed, or mistaken for investment advice.

Mitigation: Check coverage and timestamps, corroborate consequential findings, and treat results as informational rather than trading instructions.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense ClawHub release](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, API calls, Shell commands]

**Output Format:** [Natural-language market summaries and optional API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SentiSense API key; API results depend on coverage, subscription tier, and rate limits.]

## Skill Version(s):

2.21.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
