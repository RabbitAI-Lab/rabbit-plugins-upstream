## Description:

Git Repo helps agents manage Git repositories and SourceGit integration, including ghq cloning, worktree reuse, credential setup, rebase auditing, and repository layout migration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to guide repository and worktree operations, SourceGit setup, multi-account GitHub access, safe branch relocation, and PR staging workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository moves, config edits, credential handling, and cleanup paths can have high impact if applied to the wrong repository or account.

Mitigation: Review proposed move, delete, config edit, push, PR creation, and recursive cleanup actions before execution; back up SourceGit preference.json and ~/.gitconfig before changes.

Risk: Credential and token guidance can expose or persist sensitive access material if token-in-URL clone flows are used carelessly.

Mitigation: Avoid token-in-URL clone flows where possible; when unavoidable, remove credentials from remotes immediately and prefer scoped helpers or SSH configuration.

Risk: Automated Git maintenance can affect active worktrees, rebases, or unpushed work.

Mitigation: Run status, diff, dry-run, and operation-state checks first, then require explicit confirmation before modifying worktrees, pushing, creating PRs, or cleaning repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Worktree guide](worktree.md)
- [Credential helper guide](credential-helper.md)
- [SSH key guide](ssh-key.md)
- [SourceGit guide](sourcegit.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed Git commands, SourceGit preference edits, and Git configuration changes for review before execution.]

## Skill Version(s):

0.9.0 (source: ClawHub release evidence and CHANGELOG, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
