## Description:

Guides agents to simplify and declutter code while preserving behavior, with an analysis-only option for proposed changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to simplify existing code without changing behavior, or to request an analysis-only report of proposed simplifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Simplification may inadvertently change behavior or remove needed guards, comments, or public APIs.

Mitigation: Review the diff and verification results; retain guards without evidence they are unnecessary, and confirm public API changes before proceeding.

## Reference(s):

- [Simplification patterns](references/simplification-patterns.md)
- [Orchestrated simplification](references/orchestrated-simplification.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Guidance]

**Output Format:** [Code changes with a Markdown summary, or an analysis-only Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scope, key changes, verification, and residual risks; analysis-only proposals are labeled unimplemented.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
