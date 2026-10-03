## Description:

Provides read-only US stock market data and insights, including prices, sentiment, ratings, filings, options, and earnings through the SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research analysts, and other users can query US equity prices, news sentiment, insider and congressional trades, institutional holdings, and AI-generated market insights for informational research. The skill does not place trades or provide investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SentiSense API key may be disclosed or used outside its intended service.

Mitigation: Keep the key in the environment, send it only to the documented SentiSense API, and never include it in responses.

Risk: Personalized insights may reveal a user's watchlist or portfolio interests to the service and agent context.

Mitigation: Call the personalized insights endpoint only when the user explicitly requests account-specific results.

Risk: Delayed market quotes or generated insights may be mistaken for real-time prices or investment advice.

Mitigation: Label quote delays, check data timestamps, and present results as informational rather than trade recommendations.

## Reference(s):

- [SentiSense on ClawHub](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense methodology](https://sentisense.ai/methodology/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown research summaries, JSON API data, and optional curl or client examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; requires SENTISENSE_API_KEY; stock prices are approximately 15 minutes delayed.]

## Skill Version(s):

2.21.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
