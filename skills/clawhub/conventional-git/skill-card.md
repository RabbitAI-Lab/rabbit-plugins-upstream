## Description:

Conventional Commits v1.0.0 branch naming, worktree naming, and commit message standards for GitHub and GitLab projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to produce consistent branch names, worktree paths, Conventional Commit messages, and GitHub or GitLab issue-closing footers for parseable project history and changelog automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed git or gh commands may create or remove worktrees, commit changes, push branches, or modify GitHub resources.

Mitigation: Review each proposed command and its target repository, branch, and path before execution.

Risk: Incorrect branch, commit, or issue-closing guidance can make changelog generation, SemVer release automation, or issue closure inaccurate.

Mitigation: Compare generated names and messages against the project's release and contribution policy before committing or merging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/conventional-git)
- [Project homepage](https://github.com/samber/cc-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline commit examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include branch names, worktree paths, commit messages, issue-closing footers, and git or gh command suggestions.]

## Skill Version(s):

1.3.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
