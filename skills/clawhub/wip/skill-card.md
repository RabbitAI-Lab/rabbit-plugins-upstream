## Description:

WIP helps agents track in-session work progress by registering multi-step tasks, updating task status, and resuming remaining work after compaction across Claude Code and Antigravity workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep multi-step work visible, preserve task state across sessions, and decide what to proceed with, hold, defer, or delete during task cleanup and resume workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate or delete task state during cleanup and resume flows.

Mitigation: Review task changes before installation and keep external checklists or version control available for recovery.

Risk: Broad hooks and transcript scanning can inspect local workflow data and may trigger in more contexts than expected.

Mitigation: Install only in workspaces where this tracking behavior is acceptable, and prefer narrowed hook triggers before wider deployment.

Risk: External repository or deployment checks and persistent home-directory caches can affect local workflow privacy and state.

Mitigation: Limit use to trusted repositories, review configured checks and cache paths, and ask before enabling cross-skill continuation or external checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/wip)
- [Resume workflow guide](resume.md)
- [Claude Code WIP guide](claude.md)
- [Antigravity WIP guide](antigravity.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code blocks, command examples, checklist entries, and task-management instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update task-tracking artifacts, checklist entries, hook output, and local state when used by a compatible agent environment.]

## Skill Version(s):

0.7.0 (source: server release metadata and CHANGELOG.md, released 2026-09-05; SKILL.md frontmatter states 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
