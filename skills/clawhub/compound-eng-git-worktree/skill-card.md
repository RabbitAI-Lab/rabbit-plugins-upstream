## Description:

Manage Git worktrees for isolated parallel development, including creating, listing, switching, and cleaning up worktrees for concurrent reviews or feature work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to manage isolated Git worktrees for parallel implementation, code review, branch switching, and cleanup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can copy local .env files into additional worktree directories, which may duplicate secret-like configuration material.

Mitigation: Use copy-env only with trusted worktree names and paths, and review copied environment files before sharing or archiving worktrees.

Risk: The create workflow can run project dependency installers after creating a worktree.

Mitigation: Avoid running it on untrusted branches until package manifests and installer scripts have been reviewed.

Risk: The cleanup command removes inactive worktrees with force semantics.

Mitigation: Treat cleanup as destructive and verify dirty or untracked worktree contents before confirming removal.

Risk: The tool may modify repository-local ignore configuration and fetch from origin.

Mitigation: Review repository changes and remote access expectations before using the skill in sensitive or restricted repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Workflow examples](references/workflow-examples.md)
- [Troubleshooting and technical details](references/troubleshooting.md)
- [Hooks and local excludes](references/hooks-and-excludes.md)
- [Worktree manager script](scripts/worktree-manager.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to run a bundled Bash worktree manager and to report structured change summaries.]

## Skill Version(s):

4.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
