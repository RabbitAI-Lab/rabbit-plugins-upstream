## Description:

Analyze staged and committed changes and recommend split, squash, amend, staging, secret-scan, and commit-message strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to keep Git history reviewable by planning atomic commits, squashes, amendments, staging checks, and public-repository secret scans before commit or history-rewrite operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers high-impact Git rewrite, reset, rebase, push, and force-push workflows that can alter shared history or publish unintended changes.

Mitigation: Require explicit user approval before any commit, push, force-push, rebase, reset, or amend workflow, and verify staged files and CI status before publishing rewritten history.

Risk: The skill may inspect repository history, pull request metadata, staged diffs, and local rule files while preparing commit guidance.

Mitigation: Use it only in workspaces where that repository and local policy context may be reviewed by the agent.

Risk: The bundled hook guidance can create persistent behavior around commit review triggers.

Mitigation: Review the hook script and settings changes before installation, and avoid installing hook pieces unless the expected commands and scope are acceptable.

## Reference(s):

- [Commit Tidy ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/commit-tidy)
- [Hunk Split Guide](hunk-split.md)
- [Interactive Amend Guide](interactive-amend.md)
- [Soft Reset Amend Guide](soft-reset-amend.md)
- [Staging Discipline Guide](staging-discipline.md)
- [Security Scan Guide](security-scan.md)
- [Message Discipline Guide](message-discipline.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell command snippets and commit-message drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes split and squash recommendations, staging audit steps, security scan checks, and Git history rewrite cautions.]

## Skill Version(s):

0.5.2 (source: server release metadata and changelog, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
