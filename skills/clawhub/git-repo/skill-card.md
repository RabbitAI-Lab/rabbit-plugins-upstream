## Description:

Git repository and SourceGit integration for cloning with ghq, managing and reusing worktrees, migrating repository layouts, and handling multi-account Git credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to manage Git repositories and worktrees, integrate SourceGit, and handle multi-account GitHub SSH or HTTPS credential workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository, worktree, SourceGit, and Git configuration workflows can change high-impact local state.

Mitigation: Require a dry-run-style summary of exact paths, repositories, remotes, configuration files, and any push or delete actions before execution.

Risk: Credential workflows can involve GitHub credentials and account-specific authentication behavior.

Mitigation: Avoid token-in-URL cloning and review any SSH or HTTPS credential configuration before applying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Worktree guide](worktree.md)
- [Credential helper guide](credential-helper.md)
- [SourceGit integration guide](sourcegit.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and script-backed workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose repository, worktree, SourceGit, and credential changes that should be reviewed before execution.]

## Skill Version(s):

0.8.1 (source: server release metadata and changelog, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
