## Description:

Analyze staged and committed Git changes and recommend split, squash, amend, staging, secret-scan, and commit-message strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to review Git changes before committing, decide whether to split or squash commits, plan safe amend workflows, and draft disciplined commit messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: History-rewrite workflows such as reset, rebase, amend, and force-push can damage shared or protected branch history.

Mitigation: Confirm every reset, rebase, commit, and force-push with the user, and avoid shared or protected branches unless collaborators have explicitly agreed.

Risk: The bundled post-commit hook can prompt a separate code-review agent after commits if registered.

Mitigation: Register commit-review-trigger.sh only when post-commit code-reviewer delegation is desired, and disclose that behavior before enabling the hook.

Risk: Commit plans or command suggestions may be incomplete or unsafe for the current repository state.

Mitigation: Review staged files, inspect proposed commands, run the documented pre-commit checks, and verify secret-scan results before committing.

## Reference(s):

- [Commit Tidy ClawHub Page](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Hunk Split](hunk-split.md)
- [Interactive Amend](interactive-amend.md)
- [Message Discipline](message-discipline.md)
- [Security Scan](security-scan.md)
- [Soft Reset Amend](soft-reset-amend.md)
- [Staging Discipline](staging-discipline.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and commit-message drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include split or squash recommendations, staged-file checks, secret-scan commands, and commit execution plans that require user confirmation.]

## Skill Version(s):

0.5.5 (source: server release metadata and changelog, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
