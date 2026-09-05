## Description:

Tracks in-session work as persistent tasks and checklists so agents can register multi-step work before execution, recover after compaction, ask for per-item direction, and clean up completed task state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep multi-step coding or operational work visible, recoverable, and synchronized across task tools, checklist files, and WIP commits. It is most useful when an agent needs explicit task registration, progress updates, cleanup, or resume handling after context loss.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hooks and automatic workflows can inspect session logs and influence or block edit/write operations.

Mitigation: Review hook registration before enabling the skill, and use it only in workspaces where transcript inspection and edit blocking are acceptable.

Risk: The workflow can delete or rewrite task and checklist state while cleaning up completed or stale work.

Mitigation: Review task deletion paths, keep durable work records in checklist files or commits when needed, and confirm pending-item deletion decisions with the user.

Risk: The skill may run external verification commands through local tools such as GitHub CLI, git, curl, or shell scripts.

Mitigation: Limit credentials and CLI context available to the agent, and review command behavior before enabling auto-run checks in sensitive repositories.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/wip)
- [WIP Skill Definition](artifact/SKILL.md)
- [Claude Code WIP Guide](artifact/claude.md)
- [Antigravity WIP Tracking](artifact/antigravity.md)
- [Resume Workflow](artifact/resume.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code blocks, task-tool calls, checklist updates, and hook configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update task state through host task tools, markdown checklist artifacts, WIP commits, or bundled hook scripts depending on the agent environment.]

## Skill Version(s):

0.6.0 (source: ClawHub release metadata and artifact/CHANGELOG.md, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
