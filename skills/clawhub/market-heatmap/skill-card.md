## Description:

Creates a self-contained interactive HTML heatmap of a US stock index, with tiles sized by market cap and colored by price move, sentiment, SentiSense Score, mention volume, or options interest when those layers are available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market-research agents use this skill to generate a local, interactive market heatmap snapshot and a concise board summary from SentiSense data. It supports sector heatmaps, strongest and weakest movers, Market Mood views, and optional sentiment or options overlays without placing trades or modifying accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A market heatmap snapshot may be mistaken for live data, investment advice, or a trading recommendation.

Mitigation: Present the output as delayed informational market research, preserve as-of labels and disclaimers, and avoid buy, sell, forecast, or portfolio-allocation language.

Risk: The skill requires a SentiSense API key for read-only market data access.

Mitigation: Provide the key through the environment only, send it only to https://app.sentisense.ai, and do not embed the key in generated HTML or prose.

Risk: Missing overlay data can be misread as a measured neutral value.

Mitigation: Use the API's withheld-layer and missing-reading indicators, label unavailable overlays plainly, and never coerce absent values to zero.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/market-heatmap)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown summary with a self-contained HTML snapshot file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; one read-only API request per render; generated HTML embeds the board data and should not contain the API key or external network loads.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
