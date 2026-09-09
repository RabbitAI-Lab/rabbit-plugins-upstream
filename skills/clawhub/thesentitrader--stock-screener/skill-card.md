## Description:

Stock Screener helps agents translate plain-language stock and ETF screening requests into read-only SentiSense screen plans and results across sentiment, analyst, technical, momentum, price, and market-cap fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen US stocks and ETFs with SentiSense data, curated screens, custom filters, and optional watchlist scoping. The skill is intended for read-only research context, not personalized investment advice, live quotes, trading, purchases, or wallet operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the API key and screening requests, including any watchlist tickers supplied by the user, to app.sentisense.ai.

Mitigation: Install only when comfortable using SentiSense as the data provider, protect the SENTISENSE_API_KEY, and avoid submitting sensitive watchlists unless that data sharing is acceptable.

Risk: Screening output can be mistaken for financial advice, live quotes, or trade signals.

Mitigation: Present results as informational research context, show the executed plan and snapshot nature of the data, and avoid framing rows as personalized buy or sell recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-screener)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [SentiSense screener execute endpoint](https://app.sentisense.ai/api/v1/screener/execute)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON screen plans and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and sends user-directed screening requests to app.sentisense.ai; results are read-only research snapshots rather than live trade signals.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
