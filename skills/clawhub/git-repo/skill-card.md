## Description:

Git Repo helps agents manage Git repositories, worktrees, SourceGit registration, multi-account credentials, hook diagnostics, repository migration, and isolated conflict or rebase workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to inspect, reorganize, migrate, repair, and operate Git repositories and worktrees while preserving user work and coordinating with SourceGit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reorganize repositories, rewrite Git metadata, edit SourceGit settings, touch global Git credential configuration, push branches, create PRs, or remove worktrees.

Mitigation: Before high-impact topics, require an explicit plan, exact paths, backup or recovery steps, and confirmation before mv, rm, git add during rebase, preference.json edits, .gitignore edits, credential-helper changes, pushes, or worktree removal.

Risk: The security summary says safeguards are inconsistent across persistent or destructive repository and configuration changes.

Mitigation: Review proposed commands and affected files before execution, prefer dry runs where available, and keep recovery steps visible before approving changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/git-repo)
- [README](README.md)
- [Git Repo skill definition](SKILL.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, configuration guidance, and procedural checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute repository-changing Git and filesystem operations when the hosting agent has the required tools and user approval.]

## Skill Version(s):

0.10.0 (source: server release metadata and changelog, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
