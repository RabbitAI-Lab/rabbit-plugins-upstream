## Description:

Track Wall Street analyst ratings and price targets: who covers a stock and where each firm stands, upgrades and downgrades by ticker and market-wide, one analyst's profile and call history, the Street versus crowd comparison against SentiSense sentiment, and which firms moved after an earnings print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and finance-oriented agents use this skill to retrieve read-only analyst coverage, consensus price targets, rating changes, individual analyst call history, and Street-versus-crowd comparisons for US equities. Output is informational context, not personalized investment advice, trading, or portfolio management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the optional npm CLI path can execute local package code.

Mitigation: Prefer the documented REST/curl workflow or use a separately reviewed pinned CLI version before deployment.

Risk: The required SentiSense API key could be exposed through command history, logs, or process telemetry.

Mitigation: Keep the key in the environment or a protected secret store, avoid passing it on the command line, and rotate it if exposure is suspected.

Risk: Analyst ratings, price targets, and sentiment can be misread as trading advice.

Mitigation: Present results as read-only informational context, include data windows and denominators, and avoid personalized buy, sell, or portfolio recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense](https://sentisense.ai)
- [SentiSense app](https://app.sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST endpoint examples, shell commands, and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs based on SentiSense API data; requires SENTISENSE_API_KEY for full access.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
