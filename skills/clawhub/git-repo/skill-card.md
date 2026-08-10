## Description:

Git Repo helps agents manage Git repositories and SourceGit integration, including ghq cloning, worktree inventory and reuse, bare repository conversion, and multi-account SSH or credential setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to inspect, migrate, repair, and organize local Git repositories and worktrees while keeping SourceGit metadata aligned. It also guides multi-account GitHub access through SSH key mapping and credential-helper configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically change local Git repository state, SourceGit configuration, credential settings, and remote publishing flows.

Mitigation: Review each operation before execution, especially broad triggers such as clone, sourcegit, patrol, migrate, and duplicate cleanup.

Risk: Credential helper and clone workflows can affect account selection or expose sensitive access paths if token handling is not reviewed.

Mitigation: Avoid token-in-URL clone flows unless replaced with a safer credential helper, and confirm credential scope before applying account-specific Git configuration.

Risk: Migration and metadata cleanup can alter repository layout or SourceGit preference data.

Mitigation: Back up important repositories and SourceGit preference.json before migration, metadata cleanup, or broad repository management operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Skill Definition](SKILL.md)
- [Worktree Guide](worktree.md)
- [SourceGit Integration](sourcegit.md)
- [Credential Helper Guide](credential-helper.md)
- [SSH Key Guide](ssh-key.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to modify local repository state, SourceGit preferences, Git credentials, and remote publishing flows.]

## Skill Version(s):

0.7.2 (source: server release metadata and CHANGELOG, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
