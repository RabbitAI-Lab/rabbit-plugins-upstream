## Description:

Gold Tracker helps agents fetch gold price and USD/CNY data, collect relevant news, validate sourced analysis, manage threshold-based alerts, send notifications, and archive local tracking records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeromeex](https://clawhub.ai/user/jeromeex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to run a local gold-market monitoring workflow with sourced analysis checks, configurable alert thresholds, notifications, and archives. It is suited for operational tracking and briefing support, not as standalone financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured notifier commands run with the agent's environment and can send generated content outside the local workspace.

Mitigation: Review config.yaml before enabling notifications, start with the file notifier or --dry-run, and enable webhook or email only after confirming destinations and message contents.

Risk: Scheduled runs can repeatedly execute notification and fetch workflows from local configuration.

Mitigation: Keep config.yaml writable only by trusted users and avoid running scheduled notifications in environments that expose sensitive tokens.

## Reference(s):

- [Gold Tracker ClawHub page](https://clawhub.ai/jeromeex/skills/gold-tracker)
- [Publisher profile: jeromeex](https://clawhub.ai/user/jeromeex)
- [SKILL.md operation manual](artifact/SKILL.md)
- [Configuration example](artifact/config.example.yaml)
- [Generic scheduling example](artifact/examples/generic-schedule.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and YAML log/output schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local state, alert, notification, archive, and log files when its scripts are run.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
