## Description:

Tracks in-session work progress by registering multi-step tasks, updating task status, and guiding resume or cleanup decisions across Claude Code and Antigravity-style environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep multi-step coding or operations work visible, recover task state after compaction, and decide what to proceed with, split, hold, defer, or delete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic cleanup can delete task records that a user expected to keep.

Mitigation: Review the cleanup behavior before installation and require preview or confirmation for deletion targets when task records are sensitive or audit-relevant.

Risk: Status checks may touch external systems or reveal sensitive task context.

Mitigation: Use the skill only in workspaces where automatic status checks are acceptable, or modify it to ask before running gh, curl, ssh, or similar checks.

## Reference(s):

- [WIP ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/wip)
- [Claude Code WIP Guide](claude.md)
- [Antigravity WIP Tracking](antigravity.md)
- [Resume Workflow](resume.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with task-state conventions and shell hook output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to create or update task records, ask user direction questions, and run or suggest status checks for remaining work.]

## Skill Version(s):

0.4.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
