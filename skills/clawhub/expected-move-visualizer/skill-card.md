## Description:

Builds a self-contained HTML chart of modeled 30-, 60-, and 90-day expected moves for a stock or ETF using SentiSense market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market analysts use this skill to visualize modeled options-implied price ranges, volatility context, and earnings timing for stocks and ETFs. The chart is educational market context, not a trading recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating the chart requires a SentiSense API key and outbound requests at build time.

Mitigation: Provide the key only in a trusted environment and allow read-only requests to app.sentisense.ai.

Risk: Delayed, modeled market-data ranges can be mistaken for live prices or trading advice.

Mitigation: Date the snapshot and present the bands as educational estimates, not price targets or recommendations.

Risk: Free-tier previews can lack 60- and 90-day bands or leave the next report unknown.

Mitigation: Label missing horizons and unknown earnings timing explicitly rather than implying full coverage.

## Reference(s):

- [Expected Move Visualizer on ClawHub](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [Self-contained HTML chart and brief text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-viewable snapshot; free-tier previews may omit longer horizons or the next earnings date.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
