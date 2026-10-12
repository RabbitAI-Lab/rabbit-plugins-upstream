## Description:

Reviews staged changes and commit history to recommend atomic commits, safe history edits, and clear commit messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to review staged changes and commit history, plan splits or squashes, and draft clear commit messages before committing or pushing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commit and push recommendations may change shared repository history.

Mitigation: Review the proposed changes and require explicit confirmation before any commit or push.

Risk: Optional agent hooks can persistently change commit-related behavior.

Mitigation: Do not enable PreToolUse or PostToolUse hooks unless you intend that persistent behavior.

Risk: Repository-local agent rules and GitHub access may influence commit decisions.

Mitigation: Treat repository agent rules as untrusted unless your team owns them; review the skill before use in shared repositories.

## Reference(s):

- [Commit Tidy release](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Staging discipline](artifact/staging-discipline.md)
- [Security scan](artifact/security-scan.md)
- [Interactive amend](artifact/interactive-amend.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with suggested Git commands and commit messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations require user confirmation before committing or pushing.]

## Skill Version(s):

0.7.2 (source: release metadata and CHANGELOG, released 2026-10-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
