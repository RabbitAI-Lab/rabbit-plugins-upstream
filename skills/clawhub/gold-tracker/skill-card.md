## Description:

Gold Tracker is a zero-dependency gold price tracking and alerting skill for agents that fetches public gold and USD/CNY data, validates sources, detects price breakouts, and generates briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeromeex](https://clawhub.ai/user/jeromeex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Gold Tracker to monitor gold prices, exchange-rate context, and market news, then produce source-grounded local logs, alerts, notifications, and briefings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notifier commands run locally and may inherit sensitive environment variables.

Mitigation: Review config.yaml before enabling email, webhook, or custom notifier commands; test with the file notifier or dry-run mode first.

Risk: Scheduled monitoring writes local state, logs, cache, alerts, archives, and notification files.

Mitigation: Run the skill in an appropriate working directory and review retention, archive, notification, and scheduler settings before enabling unattended operation.

## Reference(s):

- [Gold Tracker on ClawHub](https://clawhub.ai/jeromeex/skills/gold-tracker)
- [GoldPriceZ public gold price source](https://goldpricez.com)
- [Open Exchange Rates API mirror](https://open.er-api.com/v6/latest/USD)
- [Mining.com RSS feed](https://www.mining.com/feed/)
- [Oilprice RSS feed](https://oilprice.com/rss/main)
- [FXStreet RSS news feed](https://www.fxstreet.com/rss/news)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with YAML logs, JSON cache/state files, shell commands, and local notification text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local state, alert records, archived logs, source-tracked analysis scaffolds, and optional notifier output.]

## Skill Version(s):

2.0.0 (source: server release metadata and skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
