## Description:

Analyze staged and committed changes and recommend split, squash, amend, staging, security-scan, or commit-message strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to keep Git history reviewable by auditing staged changes, planning atomic commits, checking public-repo secret risk, and guiding safe amend or squash workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes powerful Git history-rewrite workflows, including amend, rebase, and force-with-lease push guidance.

Mitigation: Require explicit user approval before commits, rewrites, or pushes; verify CI or branch status before any force-with-lease push.

Risk: The bundled commit-review-trigger hook can prompt a separate code-review action after successful commits, and the security evidence says that behavior is not clearly described in the main skill summary.

Mitigation: Review the hook before installation and disable it unless post-commit code-review prompts are desired.

Risk: Incorrect staging or secret handling can place unintended files or sensitive values into public Git history.

Mitigation: Run the staged-file audit and public-repo secret scan described by the skill before committing, then re-scan after sanitizing any finding.

## Reference(s):

- [Commit Tidy skill page](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [SKILL.md](artifact/SKILL.md)
- [Conflict Commit Review](artifact/conflict-commit-review.md)
- [Hunk Split](artifact/hunk-split.md)
- [Interactive Amend](artifact/interactive-amend.md)
- [Message Discipline](artifact/message-discipline.md)
- [Security Scan](artifact/security-scan.md)
- [Soft Reset Amend](artifact/soft-reset-amend.md)
- [Staging Discipline](artifact/staging-discipline.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with command blocks and commit-message drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommended file groupings, commit subjects and bodies, staging commands, validation commands, and user-confirmation gates.]

## Skill Version(s):

0.7.0 (source: server release metadata and CHANGELOG, released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
