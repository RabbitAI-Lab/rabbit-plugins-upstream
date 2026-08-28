## Description:

Track in-session work progress by registering multi-step tasks, updating task status, handling completion or abort, and supporting resume after compaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep multi-step coding work tracked across Claude Code and Antigravity sessions, including resume, cleanup, and completion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may modify task state and delete task entries during cleanup.

Mitigation: Review task changes before deployment and require explicit confirmation before deleting pending or ambiguous items.

Risk: Hook scripts can block edits or enforce registration before file changes.

Mitigation: Review or disable the hook scripts before use, and test them in a disposable workspace before enabling them for normal work.

Risk: The workflow can inspect local trackers, use home-directory state, and call repository or network tools such as gh, curl, or ssh.

Mitigation: Require confirmation before home-directory writes, transcript scanning, or external command execution, and run with the minimum local permissions needed.

## Reference(s):

- [WIP skill page](https://clawhub.ai/drumrobot/skills/wip)
- [Claude Code WIP guide](claude.md)
- [Antigravity WIP Tracking](antigravity.md)
- [Resume task cleanup workflow](resume.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown instructions with code and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update task trackers and hook configuration when used in a compatible agent environment.]

## Skill Version(s):

0.5.1 (source: server release metadata and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
