## Description:

Guides agents in retrieving read-only US stock market data, including prices, sentiment, ratings, institutional activity, options, and earnings, through the SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to query SentiSense for US equities market data and summarize sentiment, ratings, filings, options activity, and earnings. Its results are informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests send the user's key and requested tickers or screen filters to SentiSense; explicitly requested account-specific queries may disclose watchlist or portfolio context.

Mitigation: Use the key only for intended SentiSense requests and share account-specific context only when the user explicitly requests it.

Risk: Financial data or generated insights could be mistaken for investment advice.

Mitigation: Present results as informational data and leave investment decisions to the user.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense rating methodology](https://sentisense.ai/methodology/#sentisense-rating)
- [SentiSense ClawHub skill release](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Analysis]

**Output Format:** [Markdown with API request examples and data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data access; requires SENTISENSE_API_KEY for API requests.]

## Skill Version(s):

2.22.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
