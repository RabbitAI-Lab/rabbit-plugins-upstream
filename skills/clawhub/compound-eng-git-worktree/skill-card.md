## Description:

Manage Git worktrees for isolated parallel development, including creating, listing, switching, and cleaning up worktrees for reviews and feature work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage isolated Git worktrees for parallel feature development and code review while keeping the main checkout separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: New worktrees, including PR review checkouts, automatically receive copies of local .env-style files that may contain secrets.

Mitigation: Review before installing; avoid using with untrusted PRs unless secrets are removed, disposable credentials are used, or environment-file copying requires explicit opt-in.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-git-worktree)
- [Worktree integration](references/worktree-integration.md)
- [Workflow examples](references/workflow-examples.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide worktree paths and cleanup guidance.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
