## Description:

Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code quality, PRs, MRs, and diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to perform structured code reviews, audit code quality, and produce severity-ranked findings with evidence, residual risks, and a merge-readiness verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect repository files and history and run approved project verification.

Mitigation: Use it only where repository inspection and verification commands are acceptable, and grant only the tools needed for review.

Risk: Optional external reviewer use can disclose diffs or source to another vendor.

Mitigation: Require explicit consent for each external review packet and keep shared packets limited to the code needed for the review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
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
- [Scope and comparison-range resolution](references/scope-resolution.md)
- [Security Detection Patterns](references/security-patterns.md)
- [Security Test Coverage Checklist](references/security-test-coverage.md)
- [Severity Levels and Confidence Rubric](references/severity-and-confidence.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown review report with severity-ranked findings and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed verification commands, action-routing labels, residual risks, and a merge-readiness verdict.]

## Skill Version(s):

4.5.1 (source: server release metadata, changelog v4.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
