## Description:

Tracks tasks and projects in local workspace directories using progress cards, activity logs, and document indexes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and agents use this skill to create and maintain task or project progress cards, find indexed work documents, review current status, and record completion summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Moving an existing document into a task or project folder may change its original path.

Mitigation: Confirm before moving existing files when their current paths matter; otherwise index the original path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-task-progress-tracker)
- [Task card template](templates/task-card.md)
- [Project card template](templates/project-card.md)

## Skill Output:

**Output Type(s):** [Markdown, Text summaries]

**Output Format:** [Markdown progress cards with YAML frontmatter and plain-text status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local task and project files; may index documents and record completion summaries in memory files.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
