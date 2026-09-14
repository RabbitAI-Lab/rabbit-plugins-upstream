## Description:

Route TODO checklists to the right storage and enforce TaskList conversational discipline for session work, persistent files, GitHub Issues, completion reports, task priority, and media separation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to decide whether TODO items belong in session task tracking, persistent checklist files, or GitHub Issues, and to keep task status, reports, priorities, and work-record media consistent across a workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate persistent task files and includes CLI behavior that deletes task JSON files.

Mitigation: Restrict the task directories available to the agent and require explicit confirmation before deleting tasks or resuming prior-session task state.

Risk: Task priority and cross-session routing rules can influence what work the agent chooses to do next.

Mitigation: Review proposed priority changes and task transfers before broad use, especially in shared or production workflows.

Risk: The AskUserQuestion guard relies on a shell hook and sibling-file sourcing.

Mitigation: Avoid exposing the bundled CLI globally on PATH, and remove or harden the hook's sibling-file sourcing before deploying in a wider environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite)
- [ClawHub publisher profile](https://clawhub.ai/user/drumrobot)
- [Skill definition](SKILL.md)
- [Claude task CLI topic](claude-task.md)
- [Task completion report format](completion-report.md)
- [TaskList conversation IDs](conversation-id.md)
- [Task checklist sync](fix-plan-sync.md)
- [Priority prefix](priority-prefix.md)
- [Work record media separation](media-separation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, task/checklist examples, and optional JSON task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run task-file updates and shell commands when the host agent has the required permissions.]

## Skill Version(s):

0.9.1 (source: server release metadata and CHANGELOG, released 2026-09-08; frontmatter metadata says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
