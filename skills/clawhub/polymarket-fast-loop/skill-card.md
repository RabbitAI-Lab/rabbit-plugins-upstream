## Description:

Trade Polymarket BTC 5-minute and 15-minute fast markets using CEX price momentum signals via Simmer API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and run an agent-assisted Polymarket fast-market trading loop based on crypto momentum signals. It supports dry-run review, live execution, position checks, and strategy configuration for BTC, ETH, or SOL fast markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mode places real Polymarket orders and may use sensitive trading credentials.

Mitigation: Start in dry-run or paper mode, use separate credentials for this strategy, and avoid exposing a raw wallet private key unless the runtime and dependency chain are trusted.

Risk: Unattended cron or heartbeat execution can continue trading after misconfiguration or market-condition changes.

Mitigation: Set conservative position and daily-budget limits, enable live scheduling only with a clear stop or removal plan, and monitor early runs closely.

Risk: Stop-loss and take-profit monitoring may not fire before 5-minute or 15-minute markets resolve.

Mitigation: Size positions conservatively and do not rely on automated stop-losses for fast-market exits.

Risk: The default momentum strategy and parameters are not represented as a validated profitable edge.

Mitigation: Run paper mode for an extended period and tune thresholds before increasing live position sizes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-fast-loop)
- [Simmer dashboard](https://simmer.markets/dashboard?ref=sdk-skill&utm_campaign=sdk-skill)
- [Simmer Polymarket V2 migration guide](https://docs.simmer.markets/v2-migration)
- [Skill disclaimer](DISCLAIMER.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration examples, and text status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may emit dry-run summaries, live-trading commands, configuration changes, and risk guidance for operator review.]

## Skill Version(s):

1.7.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
