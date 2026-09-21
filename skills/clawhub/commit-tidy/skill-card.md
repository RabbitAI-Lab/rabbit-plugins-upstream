## Description:

Analyze staged and committed changes and recommend split, squash, amend, security-scan, or commit-message strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to keep Git history reviewable by analyzing staged, unstaged, or committed changes and proposing commit splits, squashes, amend flows, message updates, and pre-commit safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect commit history, staged diffs, repository-local rule files, and GitHub PR metadata.

Mitigation: Use it only in repositories where that inspection is appropriate, and review the analysis before acting on any recommendation.

Risk: The skill may guide commits, rebases, amends, or force-with-lease pushes after confirmation.

Mitigation: Require explicit user approval before Git history changes or pushes, and check branch state and CI status before force-with-lease operations.

Risk: Hook-style behavior can persist beyond a single repository or session when configured through user-level agent settings.

Mitigation: Review any hook setup before enabling it, prefer narrow scoping where possible, and remove or disable hooks that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Conflict commit review](artifact/conflict-commit-review.md)
- [Hunk split](artifact/hunk-split.md)
- [Interactive amend](artifact/interactive-amend.md)
- [Message discipline](artifact/message-discipline.md)
- [Security scan](artifact/security-scan.md)
- [Soft reset amend](artifact/soft-reset-amend.md)
- [Staging discipline](artifact/staging-discipline.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown recommendations with inline shell commands and commit-message drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file groupings, split or squash plans, verification steps, and confirmation gates before Git history changes.]

## Skill Version(s):

0.7.1 (source: release metadata and changelog, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
