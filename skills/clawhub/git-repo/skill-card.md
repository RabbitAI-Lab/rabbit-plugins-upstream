## Description:

Helps developers manage Git repositories and worktrees, troubleshoot hooks and account access, and integrate repositories with SourceGit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to clone and organize repositories, manage Git worktrees, diagnose hooks, and configure multi-account access and SourceGit integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Staging or pruning helpers may delete existing worktrees.

Mitigation: Back up or commit important work first; prefer dry-run and manual cleanup before executing removal.

Risk: Embedding tokens in clone URLs may expose credentials.

Mitigation: Use a credential helper or an authenticated gh workflow instead of token-bearing URLs.

Risk: Configuration workflows may alter global Git settings or SourceGit preferences.

Mitigation: Review changes to ~/.gitconfig and SourceGit preference.json before applying them.

## Reference(s):

- [git-repo on ClawHub](https://clawhub.ai/drumrobot/skills/git-repo)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may modify local repositories, worktrees, or Git and SourceGit settings.]

## Skill Version(s):

0.13.0 (source: ClawHub release and CHANGELOG; skill frontmatter lists 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
