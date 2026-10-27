## Description:

Provides AI agents with read-only access to US stock prices, sentiment, ratings, filings, institutional activity, options, and earnings data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to retrieve read-only US market data and research signals for informational stock analysis, including prices, sentiment, filings, institutional activity, options, and earnings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A temporary API key's keep link can be used by anyone who obtains it to claim the key.

Mitigation: Keep the API key and keep link private; do not place them in logs, commits, or shared screenshots.

Risk: Requested tickers, screening filters, and submitted watchlists are sent to SentiSense.

Mitigation: Send only the market data and watchlists intended for this service; use the REST API path when avoiding optional package execution and CLI configuration.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense Rating methodology](https://sentisense.ai/methodology/#sentisense-rating)
- [SentiSense website](https://sentisense.ai)
- [SentiSense ClawHub release](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON data, Guidance]

**Output Format:** [Natural-language research summaries and structured market data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only informational output; not investment advice.]

## Skill Version(s):

2.25.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
