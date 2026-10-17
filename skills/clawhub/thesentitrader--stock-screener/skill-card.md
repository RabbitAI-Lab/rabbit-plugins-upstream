## Description:

Screens US stocks and ETFs using natural-language filters across sentiment, analyst ratings, technical indicators, price, and end-of-day options data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research agents use this read-only skill to filter US stocks and ETFs, compare market signals, and review matching results alongside the screening criteria. Results are educational research context, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's API key and screening queries, including supplied watchlists, to SentiSense.

Mitigation: Use a dedicated API key and share only watchlist data you are comfortable sending to app.sentisense.ai.

Risk: Screening results may be mistaken for personalized investment advice.

Mitigation: Treat results as research context and independently verify data before making investment decisions.

## Reference(s):

- [ClawHub stock-screener release](https://clawhub.ai/thesentitrader/skills/stock-screener)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [SentiSense screener API](https://app.sentisense.ai/api/v1/screener/execute)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with screening criteria and matching stock or ETF results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results from a periodically refreshed snapshot; no trades or account changes.]

## Skill Version(s):

1.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
