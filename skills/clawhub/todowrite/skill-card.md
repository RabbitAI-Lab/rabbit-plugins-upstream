## Description:

Routes TODO checklists to the right storage and enforces TaskList conversational discipline for session tasks, file-backed TODOs, GitHub Issues, completion reports, fix-plan synchronization, priority prefixes, media separation, and the claude-task CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to route TODOs among session task tracking, durable checklist files, and GitHub Issues while keeping user-facing task reports traceable. It also provides guidance and a CLI for inspecting and changing local Claude Code or agent Task JSON files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently change local agent task records, and the bundled claude-task delete command removes a task JSON file even though the documentation describes deletion as a status change.

Mitigation: Install only when local task-file management is desired; review hook or wrapper installation, prefer explicit --dir or --session targets, and verify task state with list or show before and after destructive operations.

## Reference(s):

- [Skill overview](artifact/SKILL.md)
- [claude-task CLI](artifact/claude-task.md)
- [Completion report format](artifact/completion-report.md)
- [TaskList conversation IDs](artifact/conversation-id.md)
- [Task and checklist sync](artifact/fix-plan-sync.md)
- [Work record media separation](artifact/media-separation.md)
- [Priority prefix](artifact/priority-prefix.md)
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with command examples and optional JSON task-file operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local task JSON files through the bundled claude-task CLI when an agent chooses to use it.]

## Skill Version(s):

0.9.2 (source: server release metadata and CHANGELOG.md, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
