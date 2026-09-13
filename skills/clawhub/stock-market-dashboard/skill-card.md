## Description:

Builds a read-only stock market dashboard as a single self-contained HTML snapshot using SentiSense market data, including market mood, sentiment breadth, sector tone, watchlist analytics, filings, flows, news, analyst changes, and earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate a read-only morning market briefing dashboard as a single HTML file. It is intended for research and educational review of market mood, sentiment, attention shifts, filings, flows, story clusters, analyst activity, and earnings context, not for trading execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SentiSense API key to fetch market data.

Mitigation: Provide only the required read-only SENTISENSE_API_KEY and do not place secrets in the generated HTML snapshot.

Risk: Readers could treat the generated market dashboard as current investment advice.

Mitigation: Label the output as a static research snapshot with a generation timestamp and include the skill's not-investment-advice disclaimer.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense full API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [ClawHub publisher profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [A generated self-contained HTML file with inline CSS, optional inline JavaScript, and baked-in market data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only market-data requests; the generated dashboard should not contain secrets and is a static snapshot rather than a live trading tool.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
