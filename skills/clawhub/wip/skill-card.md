## Description:

Track in-session work progress by registering multi-step tasks, updating status, and guiding cleanup or resume decisions across Claude Code and Antigravity environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to keep multi-step work visible, preserve task state across compaction or session changes, and decide how to proceed with remaining work before execution resumes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change task and checklist state, which may hide or reshape remaining work if used without review.

Mitigation: Use it deliberately for WIP tracking, review task-list changes, and require user confirmation before deleting pending work.

Risk: Hook wiring can gate edits and alter normal agent execution flow.

Mitigation: Review hook configuration before enabling it and install hooks only in environments where register-before-execute enforcement is desired.

Risk: Repository or deployment status checks may invoke tools such as gh, curl, or ssh.

Mitigation: Avoid enabling the skill where automatic external checks, network access, or credential use are unacceptable.

Risk: Global Claude state changes can affect sessions beyond the current workspace.

Mitigation: Review any global ~/.claude configuration changes and prefer scoped setup when shared or sensitive environments are involved.

## Reference(s):

- [WIP Skill Page](https://clawhub.ai/drumrobot/skills/wip)
- [WIP Skill Definition](SKILL.md)
- [Claude Code WIP Guide](claude.md)
- [Antigravity WIP Tracking](antigravity.md)
- [Resume Workflow](resume.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown instructions with task-state updates, decision prompts, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update task lists, checklist files, or hook configuration when the host agent enables those workflows.]

## Skill Version(s):

0.5.0 (source: server release metadata and changelog, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
