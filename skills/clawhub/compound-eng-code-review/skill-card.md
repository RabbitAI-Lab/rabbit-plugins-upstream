## Description:

Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code, auditing code quality, and critiquing PRs, MRs, or diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to perform scoped, severity-ranked code reviews, audit quality and security-sensitive changes, and produce merge-readiness guidance with coverage and residual-risk notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security review reports suspicious catalog-update behavior that could persistently modify the skill's own review guidance during ordinary reviews.

Mitigation: Before installation, remove that behavior or gate it behind an explicit maintenance workflow that shows the exact patch and source evidence.

Risk: The skill may read broad repository context, run caller-authorized checks, or send code to an external reviewer when the workflow requests it.

Mitigation: Require explicit scope, test-execution authorization, and egress consent before running checks or dispatching code to any external reviewer.

## Reference(s):

- [ia-code-review Specification](SPEC.md)
- [Action Routing - 4-Tier Fix Classification](references/action-routing.md)
- [What to Check - Review Category Checklists](references/check-categories.md)
- [Composer review](references/composer-review.md)
- [Deep Review Process](references/deep-review.md)
- [Driving a long-running external reviewer subprocess](references/external-review-subprocess.md)
- [False Positive Suppression](references/false-positive-suppression.md)
- [Language-Specific Review Profiles](references/language-profiles.md)
- [PR sizing and large-diff strategy](references/pr-sizing.md)
- [Reliability Patterns](references/reliability-patterns.md)
- [Review report and integration](references/report-and-integration.md)
- [Review judgment and scope traps](references/review-judgment-traps.md)
- [Review Traps Catalog](references/review-traps-catalog.md)
- [Reviewer trust boundary](references/reviewer-trust-boundary.md)
- [Scope and mode selection](references/scope-and-mode-selection.md)
- [Scope & comparison-range resolution](references/scope-resolution.md)
- [Security Detection Patterns](references/security-patterns.md)
- [Security Test Coverage Checklist](references/security-test-coverage.md)
- [Severity Levels and Confidence Rubric](references/severity-and-confidence.md)
- [Source and boundary evidence](references/source-and-boundary-evidence.md)
- [Standard review process](references/standard-review-process.md)
- [Composer schema documentation](https://getcomposer.org/doc/04-schema.md)
- [Composer configuration documentation](https://getcomposer.org/doc/06-config.md)
- [Composer repository priorities documentation](https://getcomposer.org/doc/articles/repository-priorities.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown review report with findings, severity, confidence, coverage, residual risks, and optional shell commands for checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ready-to-merge status, CR identifiers, selected-file coverage, limitations, and reviewer routing guidance.]

## Skill Version(s):

4.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
