## Description:

Creates an interactive, self-contained US stock market heatmap with sector performance, market mood, and available sentiment overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Market researchers and other users generate a shareable US equity heatmap to inspect price moves, sector mood, and available analytical overlays without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent uses an API key to request market data.

Mitigation: Keep the key in the agent environment and avoid sharing it; the generated HTML does not contain the key.

Risk: Market prices and analytical readings can be delayed or mistaken for live investment advice.

Mitigation: Label the snapshot and each reading's as-of time; use it for research and education, not trading recommendations.

Risk: Generating the heatmap writes a local HTML file.

Mitigation: Choose and review the output path before rendering or sharing the file.

## Reference(s):

- [ClawHub market-heatmap release](https://clawhub.ai/thesentitrader/skills/market-heatmap)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Text, JSON]

**Output Format:** [Self-contained interactive HTML snapshot with an optional JSON summary and text interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The HTML contains no API key and makes no network requests when opened.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
