## Description:

Manage Git worktrees for isolated parallel development, including creating, listing, switching, and cleaning up worktrees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to isolate concurrent feature development and code reviews in separate Git worktrees while preserving other checkouts' work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic or manual copying of local .env-style files can spread credentials into additional checkouts.

Mitigation: Use --no-env for PRs, forks, origin-only branches, and third-party code; avoid copy-env unless the tree is trusted, and review copied files before committing or sharing.

Risk: Installing dependencies from an untrusted base can execute third-party code.

Mitigation: Skip installs on untrusted bases; if needed, disable lifecycle scripts and plugins and do not run pip install -e .

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Worktree workflow examples](artifact/references/workflow-examples.md)
- [Worktree troubleshooting](artifact/references/troubleshooting.md)
- [Worktree integration](artifact/references/worktree-integration.md)
- [Commit ownership](artifact/references/commit-ownership.md)
- [Hooks and local excludes](artifact/references/hooks-and-excludes.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create, switch, or remove Git worktrees and copy local environment files.]

## Skill Version(s):

5.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
