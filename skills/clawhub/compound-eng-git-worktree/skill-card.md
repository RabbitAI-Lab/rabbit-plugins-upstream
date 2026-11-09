## Description:

Manage Git worktrees for isolated parallel development. Use when creating, listing, switching, or cleaning up git worktrees, or when needing isolated branches for concurrent reviews or feature work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this tool to create and manage separate Git worktrees for parallel feature work, code review, and isolated branches. It provides commands and guidance for switching between and cleaning up those worktrees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the skill can copy secret-bearing .env files into worktrees, including through a path without trust checks; this could expose secrets when the destination contains untrusted code.

Mitigation: Install only when needed and trusted. Use --no-env for untrusted code and avoid copying .env files into PR or fork worktrees; inspect the destination before copying environment files.

Risk: The security scan was partial because two local references were unresolved, so the available evidence does not establish that the artifact is safe.

Mitigation: Review the complete artifact, including unresolved references, and complete a security review before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Skill instructions](artifact/SKILL.md)
- [Workflow examples](artifact/references/workflow-examples.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Worktree integration guidance](artifact/references/worktree-integration.md)
- [Commit ownership guidance](artifact/references/commit-ownership.md)
- [Hooks and local excludes](artifact/references/hooks-and-excludes.md)
- [Worktree manager script](artifact/scripts/worktree-manager.sh)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Operational guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance and commands for creating, listing, switching, and cleaning up Git worktrees.]

## Skill Version(s):

5.1.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
