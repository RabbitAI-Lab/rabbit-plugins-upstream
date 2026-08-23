## Description:

Expected move visualizer for stocks and ETFs: turn implied volatility into a self-contained HTML chart showing the modeled 30, 60 and 90 day expected move cone around the current price, skewed by 25-delta put and call demand, with IV rank context and the next earnings date marked inside the cone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch read-only SentiSense market data for a ticker and produce a local expected-move chart for educational market context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market-data requests.

Mitigation: Provide the key through the environment and avoid optional CLI credential storage when local key persistence is not desired.

Risk: The generated chart may be mistaken for trading advice or a forecast.

Mitigation: Present it as educational market context based on modeled expected moves, not as a personalized buy or sell recommendation.

Risk: The chart is based on a delayed, build-time market-data snapshot.

Mitigation: Use the artifact timestamp and as-of date when describing the result, and do not present it as live intraday data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance plus a self-contained HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses build-time read-only SentiSense API requests with SENTISENSE_API_KEY; the rendered HTML chart works offline from the bound data snapshot.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
