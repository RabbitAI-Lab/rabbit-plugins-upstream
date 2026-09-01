## Description:

Analyze staged/committed changes and recommend split, squash, or commit-message strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to evaluate staged or committed Git changes, decide whether to split or squash commits, draft Conventional Commit messages, and run pre-commit staging and security checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend history-rewriting Git operations such as amend, soft reset, rebase replay, or force push.

Mitigation: Require explicit user approval before executing commit, push, amend, reset, or force-push steps, and verify branch state and CI status before any force push.

Risk: The packaged post-commit review trigger and hook guidance can create persistent cross-project agent behavior.

Mitigation: Do not enable hooks or settings unless persistent behavior is intended; document how to remove any installed hook before adoption.

Risk: Pre-commit secret scanning is pattern-based and may miss secrets or flag benign examples.

Mitigation: Treat the scanner as a first-line check only; manually review staged diffs and sanitize any credential-like content before committing to public repositories.

Risk: GitHub PR lookups and public-repo language checks can expose or depend on repository metadata.

Mitigation: Use these checks only in repositories where querying repository metadata is acceptable, and avoid applying public-repo rules to private or regional projects without confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Hunk Split](hunk-split.md)
- [Interactive Amend](interactive-amend.md)
- [Message Discipline](message-discipline.md)
- [Security Scan](security-scan.md)
- [Soft Reset Amend](soft-reset-amend.md)
- [Staging Discipline](staging-discipline.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and commit-message drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend history-rewriting Git operations and hook configuration that require explicit human approval before execution.]

## Skill Version(s):

0.6.0 (source: release metadata and CHANGELOG, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
