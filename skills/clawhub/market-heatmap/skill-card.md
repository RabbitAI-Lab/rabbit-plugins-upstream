## Description:

Creates a self-contained interactive US stock market heatmap showing index constituents by sector, market cap, price movement, and available sentiment indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Market researchers and other users generate an interactive, read-only snapshot of index and sector performance to explore price movements and available market mood indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering sends a SentiSense API key to the market data service.

Mitigation: Provide the key only through the required environment variable and confirm that sharing it with app.sentisense.ai is acceptable before installation.

Risk: The skill writes a local HTML market snapshot.

Mitigation: Choose an appropriate output location and review the file before sharing it.

Risk: Market readings may be mistaken for investment advice or a trading signal.

Mitigation: Label the snapshot informational research, disclose the data's as-of times, and do not treat it as a recommendation to trade.

## Reference(s):

- [Market Heatmap on ClawHub](https://clawhub.ai/thesentitrader/skills/market-heatmap)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [HTML, JSON, Text]

**Output Format:** [Self-contained interactive HTML file, with optional JSON summary and text handoff]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local snapshot; the page makes no network requests and contains no API key.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
