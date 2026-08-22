## Description:

Expected Move Visualizer turns SentiSense options and earnings data for stocks and ETFs into a self-contained offline HTML chart showing modeled 30-, 60-, and 90-day expected-move cones with IV-rank and earnings context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market-research agents use this skill to create an offline expected-move visualization for a stock or ETF from read-only market data. The output supports educational options-volatility review and must not be presented as investment advice, a forecast, or a trade recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SENTISENSE_API_KEY to SentiSense for market-data requests.

Mitigation: Provide the key through an environment variable or host secret store, and use it only with the documented read-only SentiSense GET requests.

Risk: Optional CLI credential storage can persist the API key locally.

Mitigation: Avoid optional local credential storage unless local key persistence is acceptable for the user's machine and environment.

Risk: Expected-move charts can be misread as investment advice or forecasts.

Mitigation: Describe the output as modeled, delayed, educational market context and do not present band edges as targets, recommendations, or predictions.

Risk: The skill writes a local HTML report.

Mitigation: Tell users where the report is written and treat that local file as the expected artifact of the run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Configuration]

**Output Format:** [Self-contained HTML file plus concise text or Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY, performs read-only SentiSense GET requests at build time, and writes one local HTML report that renders offline.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
