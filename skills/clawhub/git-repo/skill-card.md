## Description:

Git repository and worktree management with SourceGit integration, covering cloning, worktree reuse, bare-repo conversion, hook diagnostics, rebase audits, and multi-account SSH or HTTPS credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Git repositories and worktrees, diagnose hook and branch state, configure SourceGit integration, and handle multi-account GitHub access. It is intended for local repository operations where command review and workspace state checks matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A bundled staging workflow can automatically force-delete existing worktrees and branches.

Mitigation: Avoid scripts/local-to-staging-pr.sh until its automatic cleanup is fixed; use dry-run cleanup flows first and review every worktree or branch removal before execution.

Risk: The skill can move repositories and edit SourceGit preference files.

Mitigation: Confirm target paths, keep backups or versioned config where practical, and close SourceGit before preference edits so changes are not overwritten.

Risk: Credential-helper guidance can modify global Git authentication behavior.

Mitigation: Review global gitconfig changes before applying them and scope credential helpers to the intended GitHub organization or repository path.

## Reference(s):

- [README](README.md)
- [Skill overview and topic index](SKILL.md)
- [Worktree guide](worktree.md)
- [Repository doctor guide](doctor.md)
- [SourceGit integration guide](sourcegit.md)
- [Credential helper guide](credential-helper.md)
- [SSH key guide](ssh-key.md)
- [Changelog](CHANGELOG.md)
- [ClawHub skill page](https://clawhub.ai/skills/git-repo)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and helper script references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local Git, ghq, GitHub CLI, shell, and SourceGit configuration operations for user review before execution.]

## Skill Version(s):

0.12.0 (source: release metadata and CHANGELOG, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
