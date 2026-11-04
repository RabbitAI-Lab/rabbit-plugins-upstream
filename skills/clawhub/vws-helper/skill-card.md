## Description:

Create and manage multi-repository workspaces with vwsd. Use for virtual workspaces, Git worktree setup, local and remote workspace sources, workspace mount/unmount, configuration, status, synchronization, push preview, diagnostics, and editor workspace files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare and manage workspaces that combine local directories with remote Git repositories. It guides workspace setup, inspection, synchronization, push previews, diagnostics, and editor workspace generation through vwsd.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Building the upstream executable without a verified source can introduce unreviewed code.

Mitigation: Review and pin the upstream source before building.

Risk: Unmounting or destroying a workspace can permanently remove uncommitted worktree changes.

Mitigation: Inspect workspace and Git state first, then commit or back up important changes before removal.

Risk: Pushing workspace changes publishes commits to a remote repository.

Mitigation: Review the push preview and use the publishing option only after authorization.

## Reference(s):

- [Virtual Workspace project homepage](https://github.com/nano-harness/virtual-workspace)
- [ClawHub vws-helper release page](https://clawhub.ai/albert-lv/skills/vws-helper)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
