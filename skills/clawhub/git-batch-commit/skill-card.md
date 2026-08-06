## Description:

Git Batch Commit helps agents split staged Git changes into focused commits, generate conventional commit messages, and, when configured, prompt before optional ClawHub/SkillHub publishing or subtree pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to organize staged repository changes into multiple focused commits with standardized messages. It is intended for commit splitting and message generation, while broader branch, PR, merge, push, and issue-closing decisions remain outside its core role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate a Git repository by reorganizing staged changes and creating commits.

Mitigation: Use dry-run or the default confirmation flow for normal work, and review proposed commit groups before allowing commits.

Risk: The --yes option can skip interactive confirmation in automation or non-interactive sessions.

Mitigation: Use --yes only in trusted repositories or controlled automation where the staged changes have already been reviewed.

Risk: Configured ClawHub/SkillHub publishing or subtree pushing can upload or push repository content after a prompt.

Mitigation: Read each publishing or subtree push prompt carefully and approve only the intended external upload or remote push.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/git-batch-commit)
- [Project homepage](https://github.com/cat-xierluo/legal-skills)
- [Commit types reference](references/commit-types.md)
- [Conventional commits reference](references/conventional-commits.md)
- [ClawHub sync check reference](references/clawhub-sync-check.md)
- [Subtree push check reference](references/subtree-push-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text, with optional JSON output from the categorization script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reorganize staged Git changes and create commits; dry-run mode reports proposed groups without committing.]

## Skill Version(s):

1.4.2 (source: server release metadata, SKILL.md frontmatter, CHANGELOG released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
