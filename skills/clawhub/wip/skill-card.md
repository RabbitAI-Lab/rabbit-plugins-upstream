## Description:

Track in-session work progress by registering multi-step work, updating task status, handling cleanup, and recovering remaining work after a compact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to keep multi-step work visible across a session, choose directions for remaining tasks, and preserve unfinished work through task tools, checklists, or WIP commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic task cleanup can remove task records without enough user control.

Mitigation: Review cleanup behavior before use and add explicit confirmation gates before deleting anything other than clearly completed task records.

Risk: The skill may run command-line checks against repositories, deployment targets, or remote services.

Mitigation: Require confirmation before SSH, curl, GitHub CLI, deployment checks, background execution, or other commands that touch external systems.

Risk: The skill can persist shared local state under the user's home directory.

Mitigation: Review any writes outside the workspace and restrict or confirm home-directory state changes before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/wip)
- [WIP skill definition](SKILL.md)
- [Resume workflow guide](resume.md)
- [Claude Code WIP guide](claude.md)
- [Antigravity WIP guide](antigravity.md)
- [Task completion detection hook](resources/wip-task-complete-detect.sh)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with task-tool calls, checklist entries, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local task records, checklist files, WIP commits, or task-completion reminders depending on the agent environment.]

## Skill Version(s):

0.4.3 (source: release metadata and CHANGELOG, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
