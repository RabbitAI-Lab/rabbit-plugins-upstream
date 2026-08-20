## Description:

Tracks agent work in progress by registering multi-step tasks, updating task status, and guiding resume or cleanup workflows across Claude Code and Antigravity environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep multi-step coding sessions organized, recover work after compaction, and decide how remaining tracked tasks should proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate task lists and checklist files, including deleting completed task records.

Mitigation: Review tracked task changes before accepting them and require explicit approval before deleting pending items.

Risk: The skill may run external checks and write persistent coordination files under the user's home directory.

Mitigation: Review or disable hook and auto-proceed behavior when every external check or persistent write should require approval.

Risk: The Antigravity AskUserQuestion emulation guidance is marked stale and needs verification.

Mitigation: Verify the current Antigravity toolset before relying on ask.md emulation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/wip)
- [Resume workflow](resume.md)
- [Claude Code WIP guide](claude.md)
- [Antigravity WIP tracking](antigravity.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with command examples and task or checklist updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to create, update, or delete task records and persistent checklist files.]

## Skill Version(s):

0.4.5 (source: server release metadata; changelog released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
