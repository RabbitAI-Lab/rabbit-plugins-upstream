## Description:

Performs structured code reviews with severity-ranked findings and an optional deep, multi-agent workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review code changes, audit code quality and security, and assess pull requests or inline diffs. It returns severity-ranked findings and a readiness verdict while preserving caller-defined scope and report format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports medium confidence and incomplete inspection: 21 of 22 components were fully inspected, one was partially inspected, and a purpose mismatch was flagged.

Mitigation: Review the reported code change behavior and the partially inspected referenced file to confirm they fit the intended review use before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Review skill instructions](SKILL.md)
- [Skill specification](SPEC.md)
- [Reviewer trust boundary](references/reviewer-trust-boundary.md)
- [Scope and mode selection](references/scope-and-mode-selection.md)
- [Scope resolution and coverage](references/scope-resolution.md)
- [Deep review workflow](references/deep-review.md)
- [Standard review process](references/standard-review-process.md)
- [Severity and confidence guidance](references/severity-and-confidence.md)
- [Security review patterns](references/security-patterns.md)
- [Security test coverage](references/security-test-coverage.md)
- [Action routing](references/action-routing.md)
- [Review report and integrations](references/report-and-integration.md)
- [External review subprocess guidance](references/external-review-subprocess.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown code review report with severity-ranked findings, coverage status, and a readiness verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the caller's scope and report format; identifies review limitations and residual risks.]

## Skill Version(s):

5.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
