## Description:

File-based todo and task tracking in the todos/ directory for creating, triaging, listing, managing, and checking persistent project work items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to maintain persistent project todos as Markdown files, including backlog items, PR feedback, dependencies, status changes, and work logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Todo entries and work logs are persisted as project files and may capture sensitive task details.

Mitigation: Do not store secrets, credentials, private customer data, sensitive logs, or unredacted personal information in todo files.

Risk: Task status, priority, issue IDs, and dependency metadata can drift from filenames if files are edited manually.

Mitigation: Verify each todo before relying on it: issue IDs should be unique and sequential, required frontmatter should be present, and status and priority should match the filename.

## Reference(s):

- [Todo Workflows](references/workflows.md)
- [Quick Reference Commands](references/quick-reference.md)
- [Todo Template](assets/todo-template.md)
- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-file-todos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files with YAML frontmatter and concise shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists project-scoped task details in repository todo files.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
