## Description:

Structural review of documents for gaps, clarity, completeness, and organization before a brainstorm, plan, spec, ADR, or other document moves to the next workflow step.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and technical writers use this workflow to review brainstorms, plans, specs, ADRs, and other documents for gaps, clarity, scope creep, and readiness for the next workflow step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads review-target documents, which may contain sensitive or private content.

Mitigation: Use it only with documents appropriate to share in the agent session, and redact secrets, private URLs, customer data, or personal information before review.

Risk: Authorized edits can change document meaning, scope, or implementation-relevant constraints.

Mitigation: Approve substantive edits deliberately, keep changes within the requested scope, and inspect the resulting document before relying on it.

Risk: The optional reader-test flow can share standalone document content with an additional agent context.

Mitigation: Use the reader test only when the document content is appropriate for that additional review context.

## Reference(s):

- [Reader test reference](references/reader-test.md)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-document-review)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown findings with optional inline document edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify review-target documents only when the user has authorized editing.]

## Skill Version(s):

4.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
