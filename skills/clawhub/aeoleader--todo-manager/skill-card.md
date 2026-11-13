## Description:

Manages to-do items by adding, viewing, completing, and deleting tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoleader](https://clawhub.ai/user/aeoleader)

### License/Terms of Use:


## Use Case:

External users use this skill to manage a simple local to-do list through /todo commands, with tasks stored in Markdown at ~/.openclaw/workspace/todos.md.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task text is stored locally in a Markdown file at ~/.openclaw/workspace/todos.md.

Mitigation: Confirm local storage is acceptable before installing and avoid entering sensitive secrets or credentials as task text.

Risk: The workflow and user-facing instructions are written in Chinese.

Mitigation: Install only if the intended users are comfortable operating a Chinese-language to-do workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aeoleader/skills/todo-manager)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and plain text command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task-management responses and uses a local Markdown todo file.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
