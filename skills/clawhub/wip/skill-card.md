## Description:

Tracks in-session agent work by registering multi-step tasks, updating progress, handling resume or cleanup flows, and restoring work after context compaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep multi-step work visible and recoverable across active sessions, compaction, and cleanup. It is aimed at Claude Code and Antigravity-style workflows that need task registration, per-item direction decisions, and progress tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes hooks that can inspect local conversation transcripts and block file edits while enforcing task registration.

Mitigation: Review hook scripts and hook registration before enabling the skill; install only when that workflow control is intended.

Risk: The workflow may create, update, or delete task records and shared state files in the user's home directory.

Mitigation: Use it only where those state changes are acceptable, and review task ledgers and checklist files during cleanup and resume.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/wip)
- [SKILL.md](SKILL.md)
- [Claude Code WIP guide](claude.md)
- [Antigravity WIP Tracking](antigravity.md)
- [Resume workflow](resume.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline command, code, and checklist examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update task tracking artifacts, checklist files, and hook-controlled reminders depending on the agent environment.]

## Skill Version(s):

0.7.3 (source: ClawHub release metadata and CHANGELOG, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
