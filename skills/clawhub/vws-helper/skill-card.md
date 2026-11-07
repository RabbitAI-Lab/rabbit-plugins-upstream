## Description:

Guides agents through creating and managing real Git-backed workspaces with vwsd, including local and remote sources, status checks, synchronization, repair, and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to set up and manage workspaces that combine local directories with remote Git repositories, including status checks, synchronization, recovery, and cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation runs a downloaded executable that was unavailable for artifact inspection.

Mitigation: Verify the installer and specific binary release through a trusted publisher source before installation.

Risk: Removing a remote worktree can permanently delete uncommitted changes; destroy also removes workspace configuration and may clear an unused cache.

Mitigation: Inspect affected worktrees and commit or back up changes before unmounting; require explicit confirmation before cleanup that discards work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/albert-lv/skills/vws-helper)

## Skill Output:

**Output Type(s):** [Shell commands, JSON configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples are tailored to the requested workspace operations.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
