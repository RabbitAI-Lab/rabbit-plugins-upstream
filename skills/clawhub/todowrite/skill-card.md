## Description:

Routes TODO checklists to the appropriate storage medium and enforces task-list conversation, reporting, synchronization, priority, and media-separation discipline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to decide whether TODOs belong in session tasks, durable files, GitHub Issues, or local task JSON, and to keep those records visible and synchronized. It also provides guidance and utilities for task completion reports, conversation-safe task references, priority prefixes, and cleanup of local task ledgers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide the agent toward persistent tracking actions in external systems such as GitHub Issues or Plane records.

Mitigation: Require explicit user confirmation before creating or updating external records, posting comments, or changing issue state.

Risk: The bundled local task CLI can create, update, delete, archive, or purge task JSON files.

Mitigation: Confirm destructive operations before running them, prefer dry-run or archive modes when pruning, and show the resulting task output to the user.

Risk: Hook registration and PATH wrappers can change how the agent asks questions or invokes local task utilities.

Mitigation: Review hook registration and wrapper scripts before enabling the skill in an agent environment.

Risk: Task state can diverge when the same work is tracked in both TaskList-style files and durable checklist files.

Mitigation: Use the skill's two-way synchronization rules so completion, deletion, transfer, split, and merge actions update both media in the same turn.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite)
- [Publisher profile](https://clawhub.ai/user/drumrobot)
- [Task completion report guidance](completion-report.md)
- [Task and checklist synchronization guidance](fix-plan-sync.md)
- [TaskList conversation ID guidance](conversation-id.md)
- [claude-task CLI guidance](claude-task.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, task-routing examples, and local CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or invoke local task-file operations, hook checks, GitHub Issue commands, and checklist edits according to user intent and confirmation boundaries.]

## Skill Version(s):

0.9.3 (source: server release metadata; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
