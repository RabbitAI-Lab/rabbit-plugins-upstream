## Description:

Routes TODO checklists to session, file, or issue storage and gives agents discipline for TaskList references, completion reporting, fix-plan sync, priority prefixes, media separation, and task JSON management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to route TODOs to the right persistence medium and keep task status, user-visible reports, and TaskList references consistent. It also provides guidance and a CLI for managing local Claude Code or agent task JSON files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent task-file mutation and deletion can remove or alter local task JSON files.

Mitigation: Enable the skill only when local task-file management is intended; require explicit user intent before add, update, delete, or transfer-style actions.

Risk: Broad path controls such as --dir, CLAUDE_TASK_DIR, or AGENT_TASK_DIR can target unintended task directories.

Mitigation: Use narrow task directories, avoid broad shared paths, and inspect the resolved directory before mutation.

Risk: Task IDs can be confused with GitHub issue or pull request numbers in user-visible text.

Mitigation: Use subject prefixes or keywords in user-visible text and avoid bare TaskList IDs unless they are clearly GitHub PR or issue references.

## Reference(s):

- [Skill overview](artifact/SKILL.md)
- [Task JSON CLI topic](artifact/claude-task.md)
- [TaskList conversation ID rules](artifact/conversation-id.md)
- [Completion report rules](artifact/completion-report.md)
- [Fix-plan sync rules](artifact/fix-plan-sync.md)
- [Priority prefix rules](artifact/priority-prefix.md)
- [Media separation guide](artifact/media-separation.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and task-file conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify local task JSON files when the included CLI is used.]

## Skill Version(s):

0.8.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
