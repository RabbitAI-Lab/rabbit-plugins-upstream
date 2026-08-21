## Description:

Stock Screener helps agents translate plain-language requests into read-only stock and ETF screen plans using SentiSense sentiment, analyst, technical, momentum, price, and market-cap signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to find and compare US stocks and ETFs that match sentiment, analyst, momentum, technical, price, size, or watchlist criteria. It is intended to expose the screen plan with results so users can review or adjust the translation from a fuzzy request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and mentions optional local credential storage.

Mitigation: Protect SENTISENSE_API_KEY, prefer environment-based credentials where appropriate, and only use local credential storage when saving the key on the machine is acceptable.

Risk: Financial screening results may be mistaken for personalized investment advice.

Mitigation: Present results as informational research context, show the screen plan, and avoid buy, sell, trading, wallet, or money-movement recommendations.

Risk: Screener data is a periodically refreshed snapshot rather than live quote data.

Mitigation: Describe prices and rows as coming from the latest screener snapshot and avoid presenting them as real-time quotes.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense Screener Execute API](https://app.sentisense.ai/api/v1/screener/execute)
- [ClawHub Stock Screener Skill](https://clawhub.ai/thesentitrader/skills/stock-screener)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands, REST examples, filter plans, and screen result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for API access; outputs are informational research context and should include visible filters, sort order, and matched counts.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
