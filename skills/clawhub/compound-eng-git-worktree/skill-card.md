## Description:

Manage Git worktrees for isolated parallel development, including creating, listing, switching, and cleaning up worktrees for concurrent feature work and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to manage isolated Git worktrees for parallel feature development and pull-request reviews without changing the active checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment files containing secrets may be copied into new worktrees, including PR review worktrees.

Mitigation: Avoid untrusted PR worktrees unless secrets are removed from those files or each copy requires explicit approval.

Risk: Dependency installs and tests in review worktrees can execute untrusted code.

Mitigation: Treat installs and tests in review worktrees as untrusted code execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Worktree workflows](artifact/references/workflow-examples.md)
- [Troubleshooting and technical details](artifact/references/troubleshooting.md)
- [Worktree integration](artifact/references/worktree-integration.md)
- [Hooks and local excludes](artifact/references/hooks-and-excludes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create and manage local Git worktrees.]

## Skill Version(s):

5.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
