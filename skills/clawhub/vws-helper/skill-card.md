## Description:

Create and manage multi-repository workspaces with vwsd. Use for virtual workspaces, Git worktree setup, local and remote workspace sources, workspace mount/unmount, configuration, status, synchronization, push preview, diagnostics, and editor workspace files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create and manage workspaces spanning local directories and remote Git repositories. It provides command and configuration guidance for mounting, inspecting, synchronizing, previewing pushes, diagnosing, and safely removing workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unmounting or destroying a workspace can permanently lose uncommitted work; destroy can also remove workspace configuration, caches, and the mountpoint.

Mitigation: Inspect `vwsd list --json`, keep backups, and confirm destructive actions before using `umount` or `destroy`.

Risk: The upstream implementation was unavailable for verification before building.

Mitigation: Review and pin the upstream source before building.

Risk: Approving a push can publish commits to a remote repository.

Mitigation: Review the `vwsd push --name <name> --json` preview before approving publication.

## Reference(s):

- [Project repository](https://github.com/nano-harness/virtual-workspace)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
