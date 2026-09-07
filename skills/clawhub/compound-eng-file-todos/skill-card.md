## Description:

File-based todo and task tracking in the todos/ directory for creating, triaging, listing, and managing persistent project work items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to keep project work items in persistent markdown todo files, including backlog triage, dependency tracking, work logs, and completion state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated todo files may contain incomplete, stale, or incorrect task details.

Mitigation: Review generated todos before relying on them and verify required sections, frontmatter, status, priority, and issue ID sequencing.

Risk: The workflow can create and rename local markdown files while managing todo status.

Mitigation: Inspect planned file changes before applying them and keep todo files under the intended project todos/ directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-file-todos)
- [Todo Workflows](references/workflows.md)
- [Quick Reference Commands](references/quick-reference.md)
- [Todo Template](assets/todo-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown instructions and todo files with YAML frontmatter]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains files in a project todos/ directory using status, priority, issue ID, tags, and dependencies.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
