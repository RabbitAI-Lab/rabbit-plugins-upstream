## Description:

Copies an agent session's conversation context into an independent branch so work can resume from a selected point without changing the original session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamingmou](https://clawhub.ai/user/yamingmou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can branch a local session at a chosen point to explore an alternative approach while retaining the original conversation and its recorded context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Forking duplicates potentially sensitive local conversation history.

Mitigation: Use only with authorized local sessions and protect the copied branch and its backups with the same care as the source.

Risk: Creating a branch writes a new session and updates local session indexes.

Mitigation: Preview with dry-run and verify the branch before relying on it; retain index backups for recovery.

Risk: A forked conversation may describe earlier file states even though workspace files and external actions remain unchanged.

Mitigation: Use version control or backups to restore files separately, and review external actions before continuing from the branch.

## Reference(s):

- [ClawHub session-fork release](https://clawhub.ai/yamingmou/skills/session-fork)
- [Session Fork English overview](https://github.com/yamingmou/session-fork-core/blob/main/README.en.md)
- [Session Fork Chinese overview](https://github.com/yamingmou/session-fork-core/blob/main/README.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and branch status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a copied local session and branch registration when executed; does not restore workspace files or undo external actions.]

## Skill Version(s):

2.4.21 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
