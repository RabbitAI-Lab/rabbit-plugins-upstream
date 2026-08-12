## Description:

Route TODO checklists to the right storage and guide agents on TaskList conversation IDs, completion reports, priority prefixes, medium synchronization, and the included claude-task CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose the right task medium for session work, persistent checklists, team-shared issues, and task JSON ledgers. It helps agents keep task state synchronized and produce visible completion reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages persistent task and checklist state, including helper tooling that can create, update, or delete local task records.

Mitigation: Install it only when persistent task management is desired, review claude-task CLI behavior before use, and surface write results to the user.

Risk: Broad requests such as move, defer, hold, or transfer can lead an agent to update the wrong task medium.

Mitigation: Confirm ambiguous transfer scope before changing state and keep task, checklist, and issue records synchronized in the same turn.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite)
- [Skill definition](artifact/SKILL.md)
- [claude-task CLI topic](artifact/claude-task.md)
- [TaskList conversation IDs](artifact/conversation-id.md)
- [Completion report format](artifact/completion-report.md)
- [Task-checklist sync](artifact/fix-plan-sync.md)
- [Priority prefix](artifact/priority-prefix.md)
- [Work record media separation](artifact/media-separation.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell command examples and task/checklist conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local task JSON files or checklist files when the agent follows the workflow.]

## Skill Version(s):

0.7.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
