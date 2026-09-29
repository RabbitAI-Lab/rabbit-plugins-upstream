## Description:

Helps developers find, inspect, organize, repair, and manage Claude Code and Antigravity sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to locate and summarize AI coding sessions, inspect context usage, and manage session history through archiving, migration, repair, or rewind.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session operations can expose or modify private conversation history, including deletion or truncation.

Mitigation: Limit access to trusted session data; use dry runs or backups and confirm destroy, migrate, purge, repair, and rewind actions first.

Risk: Hooks and automatic archive or indexing paths can process session history unexpectedly.

Mitigation: Review hook registration and disable automatic archive or indexing dispatch unless intended.

## Reference(s):

- [Session skill on ClawHub](https://clawhub.ai/drumrobot/skills/session)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with session reports and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some actions modify local session files or register hooks.]

## Skill Version(s):

0.14.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
