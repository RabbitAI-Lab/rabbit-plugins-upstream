## Description:

Helps agents create, preview, manage, and review scheduled Cargo workspace alerts over workflow telemetry, storage models, and SQL query metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to configure Cargo alerts that monitor workflow health, storage model freshness or row counts, credit usage, latency, and custom query results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Alerts can launch actions that spend credits, post externally, or run agents repeatedly during sustained breaches.

Mitigation: Preview thresholds before creation, choose the loosest useful schedule, and prefer low-cost notification actions unless a stronger action is required.

Risk: Alert writes may affect the wrong Cargo workspace or fail when the token lacks observability permissions.

Mitigation: Confirm the active workspace before writes and use credentials with the required observability read or write permission.

Risk: Invalid scope and threshold pairings, bad SQL, or deleted models can produce alert error events instead of useful monitoring.

Mitigation: Use alert preview and validate custom queries or model identifiers before committing an alert schedule.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Alert lifecycle - how evaluation and firing actually work](references/alert-lifecycle.md)
- [Alert recipes](references/examples/recipes.md)
- [Scopes and thresholds - the compatibility matrix](references/scopes-and-thresholds.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Cargo CLI commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands expect a configured cargo-ai CLI and an active Cargo workspace.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
