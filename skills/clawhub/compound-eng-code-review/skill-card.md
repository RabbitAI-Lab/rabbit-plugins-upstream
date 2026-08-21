## Description:

Provides structured code review guidance for PRs, MRs, and diffs, with severity-ranked findings and optional deep multi-agent review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to perform structured reviews of code changes, audits, PRs, MRs, and diffs. It helps scope the review, select standard or deep review mode, classify findings by severity and confidence, and produce a concise Markdown review report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reviewed repository content, diffs, comments, and tool output may contain misleading or instruction-like text.

Mitigation: The skill defines a reviewer trust boundary that treats reviewed content as evidence, not workflow instructions, and keeps active instructions authoritative.

Risk: Running verification during review can execute target-controlled scripts or newly changed commands.

Mitigation: The skill limits execution to caller-authorized verification and instructs reviewers to inspect changed command definitions before running scripts with network, privileged, destructive, or opaque behavior.

Risk: Deep review and external reviewer modes may send diffs or surrounding source to additional agents or services.

Mitigation: The skill requires read-only specialist delegation and explicit per-packet consent before external reviewer egress, including naming the files and sensitive data involved.

Risk: Review findings could be mistaken for permission to edit code, post comments, or change repository state.

Mitigation: The security evidence notes that sensitive actions are explicitly gated; the artifact also requires separate authority for source edits, VCS writes, external posts, and non-review changes.

## Reference(s):

- [ia-code-review Specification](SPEC.md)
- [Scope & comparison-range resolution](references/scope-resolution.md)
- [Reviewer trust boundary](references/reviewer-trust-boundary.md)
- [Deep Review Process](references/deep-review.md)
- [What to Check - Review Category Checklists](references/check-categories.md)
- [Severity Levels and Confidence Rubric](references/severity-and-confidence.md)
- [Action Routing - 4-Tier Fix Classification](references/action-routing.md)
- [Security Detection Patterns](references/security-patterns.md)
- [Security Test Coverage Checklist](references/security-test-coverage.md)
- [Reliability Patterns](references/reliability-patterns.md)
- [Language-Specific Review Profiles](references/language-profiles.md)
- [False Positive Suppression](references/false-positive-suppression.md)
- [Review Traps Catalog](references/review-traps-catalog.md)
- [PR sizing and large-diff strategy](references/pr-sizing.md)
- [Driving a long-running external reviewer subprocess](references/external-review-subprocess.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown review report with severity sections, file and line references, findings, residual risks, and verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shell commands for caller-authorized verification and concise guidance for review scope, action routing, and follow-up.]

## Skill Version(s):

4.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
