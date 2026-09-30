## Description:

Helps agents retrieve read-only US stock market prices, sentiment, ratings, filings, options data, earnings information, and market insights through the SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use the skill to query SentiSense for US equity market data, news sentiment, company ratings, institutional and insider activity, and earnings context. It provides information for research, not investment advice or trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and submitted market-data queries are processed by SentiSense.

Mitigation: Use a dedicated key, keep it out of logs and shared outputs, and send only queries you are comfortable sharing with SentiSense.

Risk: Personalized insights can expose account watchlist or portfolio context.

Mitigation: Request personalized account insights only when the user explicitly asks for them.

Risk: Financial data and AI-generated insights may be mistaken for investment advice.

Mitigation: Present results as informational research and let the user verify data before making financial decisions.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense ClawHub release](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, API call guidance, Shell commands, Code]

**Output Format:** [Markdown with API examples and market-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market-data queries; API key required for most endpoints, with tier-based previews and rate limits.]

## Skill Version(s):

2.19.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
