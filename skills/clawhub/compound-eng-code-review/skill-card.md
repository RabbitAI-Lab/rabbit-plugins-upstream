## Description:

Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code quality, auditing changes, and critiquing PRs, MRs, or diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to run structured code reviews that check intent, correctness, maintainability, security, reliability, test coverage, and review completeness. It supports both standard single-pass reviews and deeper multi-agent review workflows for larger or higher-risk changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deep review can pass diffs and repository context to subagents.

Mitigation: Use the skill only on code the selected agent and subagent environment are allowed to inspect, and keep reviewer tool permissions read-only unless separate authority is granted.

Risk: External reviewer CLIs may send code to another vendor.

Mitigation: Require explicit consent before invoking external reviewers, and disclose that code may leave the local environment.

Risk: Review guidance can be mistaken for authorization to edit, post, or execute commands.

Mitigation: Treat findings and fixes as proposals; grant fix, posting, or command authority only when that action is intended for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Specification](SPEC.md)
- [Action Routing](references/action-routing.md)
- [Check Categories](references/check-categories.md)
- [Deep Review Process](references/deep-review.md)
- [External Review Subprocess](references/external-review-subprocess.md)
- [False Positive Suppression](references/false-positive-suppression.md)
- [Language Profiles](references/language-profiles.md)
- [PR Sizing](references/pr-sizing.md)
- [Reliability Patterns](references/reliability-patterns.md)
- [Review Traps Catalog](references/review-traps-catalog.md)
- [Reviewer Trust Boundary](references/reviewer-trust-boundary.md)
- [Scope Resolution](references/scope-resolution.md)
- [Security Patterns](references/security-patterns.md)
- [Security Test Coverage](references/security-test-coverage.md)
- [Severity and Confidence](references/severity-and-confidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review report with severity-ranked findings, file and line evidence, verification notes, residual risks, and a merge-readiness verdict.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confidence scores, action-routing labels, and concise command suggestions for validation.]

## Skill Version(s):

4.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
