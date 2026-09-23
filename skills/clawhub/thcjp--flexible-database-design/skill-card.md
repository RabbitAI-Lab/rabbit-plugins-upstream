## Description:

Flexible Database De helps agents guide developers through flexible SQLite schema design, data archiving, search strategy, and validation for heterogeneous records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to design flexible local SQLite databases for mixed-source data, including knowledge bases, policies, reports, forms, and multi-source message records. It guides schema discovery, soft-field modeling, full-text search choices, and validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to create or modify local project files and run validation commands.

Mitigation: Review the exact files and commands before execution, especially package installation or script execution steps.

Risk: Some helper scripts referenced by the skill appear to be described but not included in the artifact.

Mitigation: Confirm required scripts exist in the target project or have the agent generate and review them before relying on the workflow.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/thcjp/skills/flexible-database-design)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with SQL, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include proposed project files, database schema changes, validation commands, and implementation guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
