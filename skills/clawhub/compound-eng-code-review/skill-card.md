## Description:

Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code, auditing code quality, and critiquing PRs, MRs, or diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to perform structured code reviews, assess PR or MR diffs, identify correctness, security, reliability, testing, maintainability, and performance issues, and produce severity-ranked findings with a merge-readiness verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads repository code, diffs, git history, PR metadata, and relevant documentation during reviews.

Mitigation: Run it only in repositories and review contexts where that access is appropriate, and avoid supplying secrets or private customer data outside the intended review scope.

Risk: Review output can include suggested fixes or commands that may be incorrect for the target repository.

Mitigation: Treat findings and commands as review guidance; validate them against project tests, maintainers' intent, and repository standards before applying changes.

Risk: The skill may use read-only specialist agents for large changes and is designed to require separate permission before write operations.

Mitigation: Keep specialist runs read-only for review tasks and require explicit authorization before fixing code, posting comments, changing branches, committing, pushing, or using write-capable APIs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [ia-code-review Specification](SPEC.md)
- [Action Routing - 4-Tier Fix Classification](references/action-routing.md)
- [What to Check - Review Category Checklists](references/check-categories.md)
- [Deep Review Process](references/deep-review.md)
- [Driving a long-running external reviewer subprocess](references/external-review-subprocess.md)
- [False Positive Suppression](references/false-positive-suppression.md)
- [Language-Specific Review Profiles](references/language-profiles.md)
- [PR sizing and large-diff strategy](references/pr-sizing.md)
- [Reliability Patterns](references/reliability-patterns.md)
- [Review Traps Catalog](references/review-traps-catalog.md)
- [Reviewer trust boundary](references/reviewer-trust-boundary.md)
- [Scope & comparison-range resolution](references/scope-resolution.md)
- [Security Detection Patterns](references/security-patterns.md)
- [Security Test Coverage Checklist](references/security-test-coverage.md)
- [Severity Levels and Confidence Rubric](references/severity-and-confidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review report with severity-ranked findings, residual risks, and a verdict; may include inline shell commands for verification.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings use stable CR identifiers, file and line evidence where available, confidence scores, and action-routing guidance.]

## Skill Version(s):

4.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
