## Description:

Git Repo helps agents manage Git repositories and SourceGit integration, including cloning through ghq, worktree inventory and reuse, repository conversion, hook diagnostics, multi-account credentials, and rebase or conflict checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to inspect, migrate, repair, and organize local Git repositories and worktrees while keeping SourceGit state and multi-account authentication aligned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some workflows can modify repositories, SourceGit settings, hooks, and credential behavior.

Mitigation: Require a dry run or explicit confirmation before mutating topics, and review proposed repository and configuration changes before execution.

Risk: Credential-helper and clone workflows can affect account selection or expose credentials if token-in-URL fallbacks are used.

Mitigation: Prefer configured credential helpers or SSH mappings, avoid token-in-URL clone fallbacks when possible, and review ~/.gitconfig changes before applying them.

Risk: Migration or cleanup workflows can move, rename, or delete repository paths and SourceGit entries.

Mitigation: Back up SourceGit preference.json and inspect migration, deletion, and destination paths before running these workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Skill definition and topic index](SKILL.md)
- [Worktree management guide](worktree.md)
- [Repository doctor guide](doctor.md)
- [Credential helper guide](credential-helper.md)
- [SSH key guide](ssh-key.md)
- [Release changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run repository, worktree, SourceGit, hook, and credential changes depending on the selected topic and user confirmation.]

## Skill Version(s):

0.10.1 (source: server release metadata and CHANGELOG, released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
