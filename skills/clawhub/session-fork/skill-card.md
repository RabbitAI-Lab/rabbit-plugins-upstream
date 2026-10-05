## Description:

Creates an independent branch of a local agent session at a chosen point while leaving the original session unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamingmou](https://clawhub.ai/user/yamingmou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can branch an in-progress conversation or task from a selected point to explore another approach without changing the original session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Branching reads local conversation history and writes new session records and index entries.

Mitigation: Use dry-run first, keep backups enabled, and only run against session stores you can restore.

Risk: A branched session may refer to earlier workspace files or actions that the fork cannot undo.

Mitigation: Use version control or backups to align workspace artifacts with the selected branch point; verify external effects separately.

## Reference(s):

- [Session Fork on ClawHub](https://clawhub.ai/yamingmou/skills/session-fork)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown text with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands creates local session records; it does not restore workspace files.]

## Skill Version(s):

2.4.20 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
