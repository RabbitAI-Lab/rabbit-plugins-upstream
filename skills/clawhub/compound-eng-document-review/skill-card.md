## Description:

Reviews planning and specification documents for structural gaps, clarity, completeness, and claims that can be checked against the code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document authors use this skill to review brainstorms, plans, specifications, and ADRs before the next workflow step, checking quality and verifying claims against the repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review may read related repository files to verify document claims.

Mitigation: Limit access to documents and repository files appropriate for the review.

Risk: An inline edit may change a document when editing is authorized.

Mitigation: Request review-only findings when no file changes are wanted; approve substantive changes before they are applied.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-document-review)
- [Optional reader test](references/reader-test.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review findings and suggested or authorized inline document edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May identify a critical improvement and offer a choice to refine or complete the review.]

## Skill Version(s):

5.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
