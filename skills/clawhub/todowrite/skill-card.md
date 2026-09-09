## Description:

Routes TODO checklists to the appropriate task, file, or issue medium and provides TaskList discipline for completion reports, subject prefixes, medium synchronization, and work-record separation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to decide where TODOs should live, keep TaskList and checklist state synchronized, and produce visible completion reports for multi-step work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Always-on task-management rules can reprioritize work or change persistent task state without the user noticing.

Mitigation: Review the hook registration and require visible confirmation lines after task add, update, or delete operations.

Risk: The bundled task CLI can modify custom task directories or task IDs supplied at runtime.

Mitigation: Avoid untrusted task IDs and custom task directories; verify the resolved task directory before mutating records.

Risk: Delete operations can remove task JSON files from disk.

Mitigation: Treat deletes as potentially permanent and confirm that the task is superseded, cancelled, or transferred before deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite)
- [TodoWrite skill definition](artifact/SKILL.md)
- [Task completion report format](artifact/completion-report.md)
- [TaskList conversation IDs](artifact/conversation-id.md)
- [Task-checklist two-way sync](artifact/fix-plan-sync.md)
- [Priority prefix](artifact/priority-prefix.md)
- [Work record media separation](artifact/media-separation.md)
- [Claude task CLI](artifact/claude-task.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Task JSON updates]

**Output Format:** [Markdown guidance with inline shell commands and optional task JSON file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, update, or delete persistent task records when the bundled CLI is used.]

## Skill Version(s):

0.9.0 (source: server release metadata and CHANGELOG, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
