## Description:

Manage Git worktrees for isolated parallel development, including creating, listing, switching, and cleaning up worktrees for concurrent reviews or feature work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage isolated Git worktrees for parallel feature development and pull-request reviews while preserving other sessions' work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic copying can place secret-bearing .env files in new worktrees, including worktrees used to review third-party changes.

Mitigation: Avoid using untrusted PR worktrees while local .env files are present; disable automatic copying until it requires explicit confirmation and uses non-secret templates or a narrow allowlist.

Risk: On untrusted branches, a symlink could redirect an environment-file copy to an unintended destination.

Mitigation: Use only trusted repositories and branches, and reject symlink destinations before copying environment files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Worktree integration](references/worktree-integration.md)
- [Workflow examples](references/workflow-examples.md)
- [Troubleshooting](references/troubleshooting.md)
- [Commit ownership](references/commit-ownership.md)
- [Hooks and local excludes](references/hooks-and-excludes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands can create or remove worktrees and copy local environment files.]

## Skill Version(s):

5.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
