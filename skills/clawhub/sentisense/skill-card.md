## Description:

Guides agents in querying SentiSense's read-only API for US stock prices, sentiment, ratings, filings, options data, earnings, and market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve and interpret read-only US equity market data from SentiSense for informational research, not to execute trades or provide investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and temporary-key keep links can expose account access if shared.

Mitigation: Keep keys and keep links out of logs, commits, and screenshots; rotate or revoke exposed keys.

Risk: Personalized insights can send account-linked watchlist or portfolio context to SentiSense.

Mitigation: Use personalized insights only when the user intends to share that context with the API.

Risk: Market insights may be mistaken for personalized investment advice.

Mitigation: Present results as informational research, not trading instructions or individualized recommendations.

## Reference(s):

- [SentiSense ClawHub release](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with API examples and market-data explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API guidance; requests require a SentiSense API key.]

## Skill Version(s):

2.23.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
