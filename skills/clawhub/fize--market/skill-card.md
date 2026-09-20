## Description:

Market retrieves date-, freshness-, and completeness-validated market quotes, K-line data, technical indicators, capital-flow data, financial statements, commodity futures data, and news for A-share, Hong Kong, and U.S. stock workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect validated market-data JSON for quotes, market snapshots, K-lines, indicators, flows, large trades, financial statements, news, and raw-observation queries. The skill supplies data for downstream analysis while leaving trading, position, and investment conclusions to the calling agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a suspicious verdict because an automatic real-time quote fallback uses unauthenticated HTTP and then caches or persists the resulting financial data.

Mitigation: Configure IWENCAI_API_KEY and prefer the iWenCai provider; treat AKShare/Sina fallback quote data as unauthenticated unless the publisher replaces the HTTP endpoint or disables that fallback.

Risk: Market-data gaps, provider failures, or incomplete fields can cause downstream reports to rely on stale or unverifiable financial data.

Mitigation: Honor nonzero command exits and structured block reasons, and require date, timestamp, field, unit, and coverage checks before using returned data.

Risk: Technical indicators, chip-cost data, fund-flow data, and news records can be mistaken for trading recommendations or verified institutional intent.

Mitigation: Use the skill output as source data only; have the calling agent separately justify any analysis and avoid treating indicator or flow values as direct buy, sell, position, or identity conclusions.

## Reference(s):

- [Market Data Scenarios](references/scenarios.md)
- [ClawHub market skill page](https://clawhub.ai/fize/skills/market)
- [iWenCai SkillHub API key setup](https://www.iwencai.com/skillhub)
- [iWenCai query2data API](https://openapi.iwencai.com/v1/query2data)

## Skill Output:

**Output Type(s):** [text, json, code, shell commands, configuration, guidance]

**Output Format:** [JSON documents from command output, with Markdown usage guidance and shell command examples in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands write retry and provider diagnostics to stderr; large raw datasets may be persisted to SQLite with compact JSON views that include raw paths.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
