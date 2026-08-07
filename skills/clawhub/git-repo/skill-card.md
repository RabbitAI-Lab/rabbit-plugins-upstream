## Description:

Git repository and SourceGit integration for cloning with ghq, managing worktrees, converting repository layouts, and handling multi-account Git credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage local Git repositories, worktrees, and SourceGit settings, including repository cloning, layout migration, conflict dry runs, and multi-account authentication troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change local repository state, worktree metadata, and SourceGit preferences.

Mitigation: Require explicit confirmation before SourceGit registration, repo moves, folder renames, deletions, bulk repairs, pushes, or PR creation.

Risk: Credential-helper workflows may affect GitHub authentication behavior on the local machine.

Mitigation: Avoid token-in-URL clone flows, prefer gh-authenticated or scoped credential-helper flows, and confirm the intended organization and account before changing credential configuration.

Risk: Repository and worktree repair scripts can alter metadata in ways that are hard to inspect after the fact.

Mitigation: Review proposed commands, inspect repository status and worktree lists first, and back up relevant Git or SourceGit configuration before applying repairs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Worktree guide](worktree.md)
- [Credential helper guide](credential-helper.md)
- [SSH key guide](ssh-key.md)
- [SourceGit guide](sourcegit.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local Git, ghq, gh, SourceGit preference, and credential-helper changes for review before execution.]

## Skill Version(s):

0.7.1 (source: server release metadata and CHANGELOG, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
