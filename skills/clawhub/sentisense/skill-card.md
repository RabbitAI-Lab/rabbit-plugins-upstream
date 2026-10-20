## Description:

Guides agents in retrieving read-only US stock market data, sentiment, filings, and market insights from the SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can guide an agent to retrieve and summarize US stock prices, sentiment, news, insider and congressional trades, institutional holdings, and analyst data for informational research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and temporary-key keep links could be exposed or misused.

Mitigation: Keep keys and keep links out of logs, shared screenshots, and commits; provide the key only when intentionally calling SentiSense.

Risk: Personalized requests may disclose account-specific watchlist or portfolio context to SentiSense.

Mitigation: Use personalized endpoints only after the user explicitly requests them.

Risk: Market data and generated insights may be mistaken for live prices or investment advice.

Mitigation: Label prices as delayed and present insights as informational, not trading recommendations.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [SentiSense ClawHub release](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code]

**Output Format:** [Markdown guidance with REST request examples and market-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data access; an API key is required for requests.]

## Skill Version(s):

2.23.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
