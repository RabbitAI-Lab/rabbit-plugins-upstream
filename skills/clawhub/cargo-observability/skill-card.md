## Description:

Helps agents create, preview, manage, and review scheduled threshold alerts for Cargo workspace telemetry, storage models, and SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to set up proactive Cargo alerts, calibrate alert scopes and thresholds, and inspect firing history when monitored workflows, models, or queries breach expected limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs @cargo-ai/cli@latest, so CLI behavior can change after review.

Mitigation: Pin and review a specific @cargo-ai/cli version before installing or running the skill in a governed environment.

Risk: Alert actions can send messages, trigger agents, call paid connectors, and repeat on a cron while a condition remains true.

Mitigation: Use least-privilege Cargo tokens, preview scopes and thresholds before creating schedules, and prefer low-cost notification actions for recurring alerts.

## Reference(s):

- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Alert lifecycle - how evaluation and firing actually work](references/alert-lifecycle.md)
- [Alert recipes](references/examples/recipes.md)
- [Scopes & thresholds - the compatibility matrix](references/scopes-and-thresholds.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cargo CLI commands are expected to emit JSON; alert actions may trigger Cargo runs when a threshold breaches.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
