## Description:

Expected move visualizer for stocks and ETFs: turn implied volatility into a self-contained HTML chart showing the modeled 30, 60 and 90 day expected move cone around the current price, skewed by 25-delta put and call demand, with IV rank context and the next earnings date marked inside the cone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to fetch read-only SentiSense market data for a ticker and produce a self-contained expected-move chart. The chart is intended for educational market context, including modeled 30, 60, and 90 day expected moves, IV rank, and earnings timing context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SENTISENSE_API_KEY to SentiSense for documented read-only market-data requests.

Mitigation: Use a SentiSense API key intended for this workflow and review the documented build-time requests before installation.

Risk: The generated chart can be mistaken for investment advice or a price forecast.

Mitigation: Present expected moves as modeled educational market context and avoid buy, sell, target, support, or resistance language.

Risk: The skill creates a local HTML report file.

Mitigation: Review the generated file before sharing; the report is designed to render offline from an inlined data snapshot.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON data binding, and a generated self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for build-time read-only API requests; finished HTML report renders offline from an inlined data snapshot.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
