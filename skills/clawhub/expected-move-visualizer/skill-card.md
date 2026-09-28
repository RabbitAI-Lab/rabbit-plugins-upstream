## Description:

Creates a self-contained HTML chart of modeled 30-, 60-, and 90-day expected moves for stocks and ETFs using implied volatility, with skew, IV rank, and earnings context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use this skill to visualize modeled expected-move ranges and compare implied volatility with historical moves around earnings. The chart provides educational research context, not a price forecast or trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key is sent to SentiSense to fetch market data.

Mitigation: Supply the key through the environment and authorize requests only to app.sentisense.ai; do not include the key in shared charts.

Risk: Modeled ranges and delayed prices could be mistaken for live quotes or trading advice.

Mitigation: Label the chart with its data date and describe ranges as modeled research context, not forecasts or trade recommendations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Analysis, Guidance]

**Output Format:** [Self-contained HTML chart with a brief text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The chart renders offline from a dated market-data snapshot; no live data is fetched when viewed.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
