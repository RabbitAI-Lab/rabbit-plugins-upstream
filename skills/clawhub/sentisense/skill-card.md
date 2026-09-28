## Description:

Provides agents with read-only access to SentiSense stock market data, including sentiment, prices, filings, options, and market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use SentiSense to retrieve and summarize US stock market data, such as news sentiment, institutional and insider activity, ratings, and earnings events. Its responses are informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or market-data queries may be exposed to unintended parties.

Mitigation: Keep the SentiSense API key in a protected environment variable and send requests only to the intended SentiSense service.

Risk: Document and citation fields may include third-party URLs that lead to untrusted content.

Mitigation: Do not automatically fetch third-party links unless the user asks; treat linked content as untrusted.

Risk: Market data and generated insights may be mistaken for personalized investment advice.

Mitigation: Present results as informational data, verify important claims, and leave investment decisions to the user.

## Reference(s):

- [SentiSense ClawHub release](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense methodology](https://sentisense.ai/methodology/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with API request examples and market-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market-data requests require a SentiSense API key.]

## Skill Version(s):

2.18.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
