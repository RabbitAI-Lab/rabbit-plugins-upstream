## Description:

Commit Tidy helps agents analyze staged, unstaged, and committed Git changes and recommend split, squash, amend, staging, secret-scan, and commit-message strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to keep Git history reviewable by planning atomic commits, squash candidates, safe amend flows, explicit staging, pre-commit secret checks, and Conventional Commit messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide commit rewriting and force-push workflows, which can disrupt shared Git history if used without review.

Mitigation: Require explicit user approval before commit, amend, rebase, or push actions, and verify CI status before any force-push workflow.

Risk: The bundled commit-review trigger can launch or prompt a code-review workflow after successful commits and expose repository context.

Mitigation: Register the hook only with explicit opt-in and confirm what repository path and commit SHA will be passed to the review agent.

Risk: The skill inspects repo-local rules and GitHub repository state, so recommendations may depend on local configuration and permissions.

Mitigation: Review proposed commands before execution and limit GitHub checks to the intended repository and branch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Hunk Split](hunk-split.md)
- [Interactive Amend](interactive-amend.md)
- [Message Discipline](message-discipline.md)
- [Security Scan](security-scan.md)
- [Soft Reset Amend](soft-reset-amend.md)
- [Staging Discipline](staging-discipline.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and commit-message drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed Git history-rewrite steps, staged-file checks, secret-scan commands, and commit or PR message text.]

## Skill Version(s):

0.5.4 (source: server release metadata and changelog, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
