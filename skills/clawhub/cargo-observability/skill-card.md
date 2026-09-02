## Description:

Helps agents create, preview, manage, and review scheduled Cargo observability alerts over workflow telemetry, storage models, and SQL query results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to configure Cargo alerts that monitor workflow health, model freshness, row counts, custom SQL metrics, and credit usage, then inspect alert status and firing history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent alerts can read workspace telemetry or warehouse query results and automatically run agents, tools, or connectors when thresholds breach.

Mitigation: Preview alerts before creation, verify the active Cargo workspace with whoami, use the narrowest practical scope, and choose the loosest useful schedule.

Risk: Alert actions can trigger recurring paid runs or high-cost provider actions if thresholds are too sensitive or schedules are too frequent.

Mitigation: Calibrate thresholds from preview results, prefer low-cost notification actions, and avoid high-cost actions unless recurring paid runs are intended.

Risk: Invalid scope and threshold pairings, bad SQL, or deleted models can produce alert error events instead of useful monitoring.

Mitigation: Check the scope and metric compatibility matrix, validate SQL separately when possible, and use alert preview before create or update.

## Reference(s):

- [Cargo Observability ClawHub Page](https://clawhub.ai/cargo-ai/skills/cargo-observability)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Alert lifecycle - how evaluation and firing actually work](references/alert-lifecycle.md)
- [Scopes and thresholds - the compatibility matrix](references/scopes-and-thresholds.md)
- [Alert recipes](references/examples/recipes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cargo CLI commands that create or update persistent scheduled alerts and actions.]

## Skill Version(s):

1.0.2 (source: release evidence, SKILL.md frontmatter, skill-metadata.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
