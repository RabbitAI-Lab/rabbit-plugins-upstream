## Description:

Git repository and SourceGit integration for cloning via ghq, managing worktrees, recovering repository metadata, and handling multi-account GitHub access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to guide Git and SourceGit workflows, including worktree reuse, repository migration, credential/account setup, hook diagnosis, isolated staging, and rebase audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent repository, GUI configuration, credential, and filesystem changes.

Mitigation: Review workflows that edit SourceGit preferences, .gitignore, global Git credentials, SSH settings, worktree metadata, or remotes before allowing execution.

Risk: Some workflows are broad or automatic when paths, accounts, or repositories are ambiguous.

Mitigation: Prefer manual execution or dry runs until the target path, account, repository, and remote operation are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Skill definition and topic index](SKILL.md)
- [Worktree workflow guide](worktree.md)
- [SourceGit integration guide](sourcegit.md)
- [HTTPS credential helper guide](credential-helper.md)
- [SSH key mapping guide](ssh-key.md)
- [Git hooks troubleshooting guide](githooks.md)
- [Repository to ghq migration guide](to-ghq.md)
- [Bare repository conversion guide](to-bare.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct Git, ghq, SourceGit, SSH, credential, worktree metadata, and filesystem operations depending on the active agent permissions.]

## Skill Version(s):

0.9.1 (source: release evidence and CHANGELOG, released 2026-08-26; artifact frontmatter says 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
