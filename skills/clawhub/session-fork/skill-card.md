## Description:

Duplicate any work-in-progress into an independent branch, carrying context, confirmed conclusions, completed steps, and tool results while leaving the original line untouched.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamingmou](https://clawhub.ai/user/yamingmou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Session Fork to create independent branches of an in-progress conversation, task, plan, coding session, writing session, or research workflow. It is intended for local agent environments where the user wants to resume from an earlier context without changing the original session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can duplicate sensitive local conversation history.

Mitigation: Use it only for sessions that should be copied, run dry-run first, and install from a pinned reviewed commit or hash-pinned package.

Risk: A `current` session reference may resolve to the wrong source session in some adapters.

Mitigation: Prefer explicit session IDs or request IDs, verify the printed source session name before landing a branch, and stop if it does not match the intended conversation.

Risk: Forking restores session context but does not roll back workspace files or external side effects.

Mitigation: Use git commits, worktrees, stashes, snapshots, or backups to align workspace artifacts with the intended branch point.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yamingmou/skills/session-fork)
- [Session Fork English overview](https://github.com/yamingmou/session-fork-core/blob/main/README.en.md)
- [Session Fork Chinese overview](https://github.com/yamingmou/session-fork-core/blob/main/README.md)
- [Session Fork releases](https://github.com/yamingmou/session-fork-core/releases)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local branch session files and session index entries when executed; dry-run validates the selected branch point before landing a branch.]

## Skill Version(s):

2.4.13 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
