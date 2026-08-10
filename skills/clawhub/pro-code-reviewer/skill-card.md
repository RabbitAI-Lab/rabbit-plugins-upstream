## Description:

Review code changes against Android, iOS, TypeScript, Go, general, and agent-skill review rules with structured severity findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[timeaground](https://clawhub.ai/user/timeaground)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to review local commits, staged or unstaged changes, branches, and GitHub or GitLab pull requests before merging. It provides platform-aware findings with severity, file locations, reasoning, and suggested fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads code diffs and nearby changed-code context, which may expose sensitive code or secrets to an AI assistant.

Mitigation: Install and run it only on repositories whose code can be reviewed by the assistant, and avoid using it on repositories containing secrets or sensitive code that should not be shared.

Risk: Inside a git repository, saying "review" is intended to review uncommitted changes.

Mitigation: Use explicit review scopes such as "review staged", a commit hash, a branch comparison, or a pull request URL when the intended scope is narrower.

Risk: Remote pull request review requires reading repository or PR diffs from declared code hosting domains.

Mitigation: Use remote PR review only when access to GitHub or GitLab diffs is acceptable for the repository being reviewed.

## Reference(s):

- [Code Reviewer ClawHub page](https://clawhub.ai/timeaground/skills/pro-code-reviewer)
- [General Review Rules](references/review-general.md)
- [Android Review Rules](references/review-android.md)
- [iOS Review Rules](references/review-ios.md)
- [TypeScript Review Rules](references/review-typescript.md)
- [Go Review Rules](references/review-go.md)
- [Agent Skill Security Review Rules](references/review-skill-vetter.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown review report with severity-ranked findings, file locations, reasoning, and fix suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only review output; findings are organized by P0, P1, and P2 severity.]

## Skill Version(s):

1.3.1 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
