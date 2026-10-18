## Description:

Helps Cargo workspace users configure and review scheduled alerts for workflow telemetry, storage models, and SQL-based metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to preview, create, manage, and review threshold alerts for Cargo workflows and data models, including notifications when monitored metrics breach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled alert actions can create repeated paid runs.

Mitigation: Preview and narrowly scope alerts, stage them disabled, and choose conservative schedules and low-cost actions.

Risk: Alert changes require workspace write permissions and can monitor broader data than intended.

Mitigation: Confirm the active workspace, grant only needed observability permissions, and review query scope before enabling alerts.

Risk: The suggested CLI install uses an unpinned latest package version.

Mitigation: Review and trust the Cargo CLI package before installation, and pin an approved version when reproducibility matters.

## Reference(s):

- [Cargo observability skill listing](https://clawhub.ai/cargo-ai/skills/cargo-observability)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Alert lifecycle](artifact/references/alert-lifecycle.md)
- [Alert recipes](artifact/references/examples/recipes.md)
- [Scopes and thresholds](artifact/references/scopes-and-thresholds.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with CLI examples and concise summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The Cargo CLI returns JSON; configured alerts can record events and trigger actions.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
