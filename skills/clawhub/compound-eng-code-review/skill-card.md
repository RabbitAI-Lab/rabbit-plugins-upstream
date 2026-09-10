## Description:

Provides structured, severity-ranked code review for PRs, diffs, and repository changes, with standard and deep multi-agent review modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review code changes, audit repository behavior, classify findings by severity and confidence, and decide whether a change is ready to merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad repository inspection and verification steps can exceed the intended review scope if the scope is not frozen first.

Mitigation: Resolve the review scope up front, enumerate selected files, and report skipped or incomplete coverage before giving a merge verdict.

Risk: External reviewer workflows may send a named diff or files to another provider.

Mitigation: Use external reviewers only with explicit egress consent and bind the request to the approved diff or files.

Risk: Review findings can be wrong or overstate certainty when based only on pattern matching.

Mitigation: Require concrete source evidence, severity based on demonstrated impact and reachability, and residual-risk disclosure for consequential uncertainty.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Specification](SPEC.md)
- [Reviewer Trust Boundary](references/reviewer-trust-boundary.md)
- [Scope and Mode Selection](references/scope-and-mode-selection.md)
- [Scope and Comparison Range Resolution](references/scope-resolution.md)
- [Standard Review Process](references/standard-review-process.md)
- [Deep Review Process](references/deep-review.md)
- [Severity Levels and Confidence Rubric](references/severity-and-confidence.md)
- [Security Detection Patterns](references/security-patterns.md)
- [Security Test Coverage Checklist](references/security-test-coverage.md)
- [Review Report and Integration](references/report-and-integration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown review report with findings, scope, verification notes, residual risks, and merge verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested verification commands and explicit limitations for skipped or incomplete coverage.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
