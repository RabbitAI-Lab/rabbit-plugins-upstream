## Description:

Guides behavior-preserving code simplification and produces analysis-only reports when edits are not requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to simplify code while preserving behavior, or to identify potential improvements without making edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Simplifying sensitive code can unintentionally change behavior or remove protective checks.

Mitigation: Review changes in authentication, protocol, financial, and public API code; retain guards unless their removal is supported by evidence.

Risk: A proposed refactor may appear equivalent without covering edge cases.

Mitigation: Require relevant tests or explicit confirmation when behavior parity is uncertain, and distinguish unimplemented proposals from verified edits.

## Reference(s):

- [Simplification patterns](references/simplification-patterns.md)
- [Orchestrated simplification](references/orchestrated-simplification.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Guidance]

**Output Format:** [Code edits or a Markdown analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Applied changes include verification results and residual risks; analysis-only reports label proposals as unimplemented.]

## Skill Version(s):

5.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
