## Description:

BigA provides A-share stock screening, market analysis, quantitative scoring, timing signals, stock-pool monitoring, and scheduled buy/sell alert summaries for users tracking Chinese equity markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to monitor A-share market conditions, maintain a focused stock pool, and generate concise trading-watch summaries with technical timing, sector, catalyst, and risk notes. It is intended as informational investment analysis and alerting, not as a substitute for human financial judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create scheduled jobs and send recurring stock-alert messages to a configured channel.

Mitigation: Review the cron schedule, timeout, channel, and recipient before installation, and install only when recurring A-share alerts are intended.

Risk: The skill uses web searches and local memory to prepare stock-pool and market summaries.

Mitigation: Use it only in workspaces where storing stock preferences locally and searching market context are acceptable.

Risk: Generated stock analysis can be incomplete, stale, or unsuitable for a user's financial situation.

Mitigation: Treat outputs as informational market monitoring, verify material data independently, and require human review before any investment decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/biga)
- [Technical timing score](artifact/references/technical-timing-score.md)
- [Sector matrix](artifact/references/sector-matrix.md)
- [User preferences](artifact/references/user-preferences.md)
- [Cron templates](artifact/references/cron-templates.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown alert summaries with optional segmented text, JSON scan output, and shell commands for scheduled setup or updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include recurring market alerts, stock-pool summaries, buy/sell watch labels, timing scores, and risk disclaimers.]

## Skill Version(s):

6.0.20 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
