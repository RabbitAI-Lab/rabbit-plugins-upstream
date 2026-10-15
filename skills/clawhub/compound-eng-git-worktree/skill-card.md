## Description:

Manage Git worktrees for isolated parallel development, including creation, listing, switching, and cleanup for concurrent feature work and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create and manage isolated Git worktrees for parallel feature development and code reviews without disturbing another checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: New worktrees may receive copies of local .env files containing secrets.

Mitigation: Use --no-env for pull requests, forks, and third-party code, or whenever copied secrets are unnecessary.

Risk: Copied .env files and installed dependencies remain on disk until explicitly disposed of.

Mitigation: Review and remove those files and dependencies when the worktree is no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Worktree integration](references/worktree-integration.md)
- [Workflow examples](references/workflow-examples.md)
- [Commit ownership](references/commit-ownership.md)
- [Hooks and local excludes](references/hooks-and-excludes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report worktree paths, branch status, and cleanup steps.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
