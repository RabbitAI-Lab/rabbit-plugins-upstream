## Description:

Duplicate any work-in-progress into an independent branch: context, confirmed conclusions, completed steps, and tool results come along while the original line stays untouched; workspace artifacts are not rolled back unless they have their own version history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamingmou](https://clawhub.ai/user/yamingmou)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to fork a running session or task into an independent branch, preserving prior context and tool results so alternate approaches can continue without changing the original session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and modifies local agent session stores, which can contain sensitive context and tool results.

Mitigation: Install only where local session-store access is intended, run --dry-run first, and prefer explicit --session or --request-id values over ambiguous current-session selection.

Risk: A fork copies session context but does not roll back workspace files or external side effects.

Mitigation: Tell users that workspace artifacts only align with the fork point when they have independent version history such as git, snapshots, or backups.

Risk: A fork created from the wrong source session or split point can preserve the wrong context.

Mitigation: Review the Source and Split lines before execution and keep the automatic backups until the new branch opens correctly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yamingmou/skills/session-fork)
- [English overview](https://github.com/yamingmou/session-fork-core/blob/main/README.en.md)
- [Chinese overview](https://github.com/yamingmou/session-fork-core/blob/main/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with inline shell commands and CLI status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or register local session-branch records; dry-run validates the intended fork without landing a branch.]

## Skill Version(s):

2.4.18 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
