## Description:

WIP helps agents track in-session work by registering, updating, resuming, and cleaning up task checklists across supported agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT License

## Use Case:

Developers and agent operators use this skill to keep multi-step work visible, recover remaining tasks after compaction or session changes, and enforce task registration before execution when configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hook resources may inspect prompts or transcripts and block edit/write actions until task registration occurs.

Mitigation: Review hook behavior before installing and enable the enforcement hooks only in environments where register-before-execute blocking is desired.

Risk: Cross-session state and task cleanup reminders can affect future agent behavior beyond simple checklist tracking.

Mitigation: Confirm the expected task and home-directory state paths during setup, and remove or disable the hooks if persistent cross-session coordination is not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/wip)
- [WIP Skill Definition](SKILL.md)
- [Resume Workflow Guide](resume.md)
- [Claude Code WIP Guide](claude.md)
- [Antigravity WIP Guide](antigravity.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code blocks, command examples, and hook resource files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes task-tracking procedures and optional hook resources; does not execute user work by itself.]

## Skill Version(s):

0.7.2 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
