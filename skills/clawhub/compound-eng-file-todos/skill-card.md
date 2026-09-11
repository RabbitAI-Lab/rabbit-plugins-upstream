## Description:

File-based todo and task tracking in the todos/ directory for creating, triaging, listing, and managing project work items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to maintain persistent Markdown todo files for project planning, backlog management, dependency tracking, triage, and work logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Todo files and work logs are stored persistently in the repository or workspace.

Mitigation: Avoid recording secrets, credentials, private customer data, sensitive internal links, or machine-specific paths in todo files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-file-todos)
- [Todo Workflows](references/workflows.md)
- [Quick Reference Commands](references/quick-reference.md)
- [Todo Template](assets/todo-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown todo files with YAML frontmatter and inline shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses sequential issue IDs, status and priority filename fields, dependency metadata, acceptance criteria, and work-log sections.]

## Skill Version(s):

4.5.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
