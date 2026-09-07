## Description:

Git Repo helps agents manage Git repositories and SourceGit integration, including ghq cloning, worktree reuse, repository conversion, hook diagnostics, and multi-account SSH or HTTPS credential workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to inspect, repair, migrate, and organize Git repositories and worktrees while coordinating with SourceGit, ghq, GitHub credentials, SSH keys, hooks, and related local shell helpers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential workflows can expose tokens if token-in-URL clone fallbacks or copied commands are used carelessly.

Mitigation: Avoid token-in-URL fallbacks, prefer SSH keys or credential helpers, and redact credentials from commands, logs, and documentation.

Risk: Repository and application configuration workflows can alter SourceGit preferences, global gitconfig, project gitignore files, or hook behavior.

Mitigation: Require explicit confirmation before configuration edits and review the exact diff or setting change before applying it.

Risk: Worktree movement, cleanup, branch deletion, repository migration, and PR creation can change or remove local Git state.

Mitigation: Run status and operation-state checks first, confirm the target repository and worktree, and require explicit approval before destructive or publishing actions.

Risk: Bundled shell scripts perform powerful local Git and filesystem operations.

Mitigation: Inspect script behavior before running it and execute commands only in the intended repository with the expected account and remote.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Topic Index](SKILL.md)
- [Worktree Guide](worktree.md)
- [Repository Doctor Guide](doctor.md)
- [SourceGit Guide](sourcegit.md)
- [Credential Helper Guide](credential-helper.md)
- [SSH Key Guide](ssh-key.md)
- [Rebase Audit Guide](rebase-audit.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and occasional script or configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference local Git, ghq, gh, SSH, SourceGit, and bundled shell scripts; users should review proposed operations before execution.]

## Skill Version(s):

0.11.0 (source: server release metadata and CHANGELOG, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
