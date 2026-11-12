## Description:

Analyzes stock-market sentiment from local CSV market data using a four-dimension model, producing 0-100 scores, market states, and planner-facing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to turn user-provided market CSV data into market sentiment reports, trend summaries, JSON outputs, and stock-planner market parameters. It is intended for decision support and requires human review before any trading use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill produces trading-oriented suggestions that could be mistaken for investment advice.

Mitigation: Review outputs manually and do not connect planner parameters to automated trading without separate human confirmation and risk controls.

Risk: Scores and market states depend on the completeness and accuracy of the input CSV data.

Mitigation: Validate market data sources, column mappings, and freshness before relying on generated sentiment reports.

## Reference(s):

- [Market Sentiment skill page](https://clawhub.ai/wwumit/skills/market-sentiment)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Terminal text reports with optional JSON files and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include sentiment scores, dimension details, market state labels, planner parameters, suggested position sizing, and thresholds.]

## Skill Version(s):

1.1.0 (source: server release metadata, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
