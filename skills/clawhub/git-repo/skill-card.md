## Description:

Git repository and worktree management with SourceGit integration for cloning, diagnosing hooks, managing credentials, converting repository layouts, and reusing or repairing worktrees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to manage Git repositories and worktrees, diagnose hook and credential issues, migrate repository layouts, and coordinate SourceGit configuration during agent-assisted development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository, worktree, or SourceGit configuration changes can move, rewrite, or remove local state.

Mitigation: Use the skill only in repositories where the workflow is understood, inspect proposed commands, and require dry runs or explicit confirmation before cleanup, migration, or config-changing actions.

Risk: Credential workflows can select or expose the wrong GitHub account or token if used carelessly.

Mitigation: Prefer pinned credential or SSH configuration, avoid token-in-URL cloning, and review account mappings before applying credential changes.

Risk: Automation may push branches, open pull requests, or change repository state beyond local diagnostics.

Mitigation: Review generated push and PR commands before execution and limit use to trusted repositories and expected branches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Skill guide](SKILL.md)
- [Worktree workflow](worktree.md)
- [Repository doctor](doctor.md)
- [Credential helper](credential-helper.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include repository-changing procedures that should be reviewed before execution.]

## Skill Version(s):

0.11.1 (source: server release metadata and CHANGELOG, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
