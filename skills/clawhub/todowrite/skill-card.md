## Description:

TodoWrite routes TODO checklists to session tasks, files, or issues and enforces task-list conversation, completion-report, synchronization, priority, and media-separation discipline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to decide where TODO work should live, keep session tasks and persistent checklists synchronized, and produce visible completion reports for multi-step work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent authority to mutate persistent task and checklist state, including deleting stale or transferred tasks.

Mitigation: Review task and checklist changes before relying on them, and prefer explicit confirmation before deleting tasks, cleaning stale prior-session tasks, or creating external tracking issues.

Risk: Installation or use may add active task-management behavior through an AskUserQuestion hook or a local command wrapper.

Mitigation: Inspect whether the AskUserQuestion hook or ~/.local/bin wrapper is registered, and enable them only in environments where persistent task-management behavior is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite)
- [TodoWrite skill definition](artifact/SKILL.md)
- [Task completion report guidance](artifact/completion-report.md)
- [Task and checklist sync guidance](artifact/fix-plan-sync.md)
- [Claude task CLI guidance](artifact/claude-task.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with command examples and Python or shell resource scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create or update task JSON files, checklist files, and issue-tracking commands.]

## Skill Version(s):

0.8.2 (source: server release metadata and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
