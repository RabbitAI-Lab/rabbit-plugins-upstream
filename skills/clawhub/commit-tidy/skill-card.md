## Description:

Analyze staged and committed changes and recommend split, squash, or commit-message strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect staged, unstaged, and committed Git changes, then plan atomic commits, squashes, amendments, and commit messages. It is especially suited to workflows that need explicit staging checks, public-repository secret scans, and non-interactive Git command guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide history-changing Git operations such as reset, rebase, amend, squash, and force-push.

Mitigation: Require explicit user confirmation before any history rewrite or force-push, and verify branch state and CI status before proceeding.

Risk: The bundled post-commit review trigger can hand off repository path and commit SHA to a code-reviewer agent after successful commits.

Mitigation: Install or enable the trigger only when automatic post-commit review handoff is intended, and review the hook behavior before use.

Risk: Persistent agent configuration changes can affect future repository actions beyond the current task.

Mitigation: Require explicit confirmation before changing user-level agent settings such as ~/.claude/settings.json.

## Reference(s):

- [Commit Tidy ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Commit Tidy Skill Definition](artifact/SKILL.md)
- [Changelog](artifact/CHANGELOG.md)
- [Hunk Split](artifact/hunk-split.md)
- [Interactive Amend](artifact/interactive-amend.md)
- [Message Discipline](artifact/message-discipline.md)
- [Security Scan](artifact/security-scan.md)
- [Soft Reset Amend](artifact/soft-reset-amend.md)
- [Staging Discipline](artifact/staging-discipline.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commit split or squash plans, commit subject and body drafts, staged-file checks, and Git command sequences when execution is requested.]

## Skill Version(s):

0.5.1 (source: server release metadata and CHANGELOG, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
