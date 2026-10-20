## Description:

Provides read-only SentiSense stock sentiment, market mood, smart-money activity, and related insights for US equities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and other users can review stock sentiment, market mood, and reported positioning signals as informational context rather than personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker queries and market-data requests are sent to SentiSense over the network using an API key.

Mitigation: Confirm that sharing these requests with SentiSense is acceptable and provide the key only through the expected environment variable.

Risk: Sentiment, positioning signals, and delayed or partial data can be mistaken for investment advice or a complete current picture.

Mitigation: Treat results as informational, check freshness and preview coverage, and do not use them as personalized buy or sell recommendations.

## Reference(s):

- [Stock Sentiment on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with dated market-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Informational, read-only analysis; distinguish delayed prices and partial previews from complete, current data.]

## Skill Version(s):

0.6.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
