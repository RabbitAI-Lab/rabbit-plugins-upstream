## Description:

Creates a self-contained HTML chart of modeled 30-, 60-, and 90-day expected stock or ETF moves from implied-volatility data, with earnings and volatility context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and other users can visualize modeled expected price ranges for stocks and ETFs and compare them with IV rank and earnings context. The chart supports educational analysis, not trading decisions or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Building the report sends a ticker and SentiSense API key to app.sentisense.ai.

Mitigation: Confirm the user accepts that data transfer before running the skill; keep the API key private.

Risk: Delayed, modeled price bands could be mistaken for live quotes or investment advice.

Mitigation: Label figures as modeled and educational, show their data date, and avoid presenting band edges as predictions or trade recommendations.

## Reference(s):

- [Expected Move Visualizer on ClawHub](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [Self-contained HTML chart and brief text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-viewable snapshot built from read-only market data; modeled, delayed figures rather than live prices or forecasts.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
