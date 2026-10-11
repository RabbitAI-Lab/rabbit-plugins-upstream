## Description:

Simplifies and declutters code while preserving behavior, or reports proposed simplifications without editing when asked for analysis only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to simplify existing code without changing its behavior, or to receive an analysis-only report of proposed improvements and verification needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Code simplifications can inadvertently change behavior or interfaces.

Mitigation: Review diffs and compare relevant tests, type checks, and observable outputs before accepting edits.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-simplifying-code)
- [Simplification patterns](references/simplification-patterns.md)
- [Orchestrated simplification](references/orchestrated-simplification.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Guidance]

**Output Format:** [Code edits with a Markdown summary, or a Markdown analysis-only report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scope, verification results, and residual risks after edits; analysis-only reports identify unimplemented proposals and required checks.]

## Skill Version(s):

5.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
