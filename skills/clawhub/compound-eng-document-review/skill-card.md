## Description:

Structural review of documents for gaps, clarity, completeness, and organization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and technical writers use this workflow to review brainstorms, plans, specs, ADRs, and similar documents for clarity, completeness, scope control, and readiness before implementation or the next workflow step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may inspect the wrong or sensitive planning document if invoked without a specific path in a workspace containing multiple documents.

Mitigation: Specify the exact document path before invoking the skill, especially in sensitive or document-heavy workspaces.

Risk: Substantive restructuring or meaning changes could alter author intent if accepted without review.

Mitigation: Review requested edits before approving substantive restructuring or meaning changes.

## Reference(s):

- [ia-document-review Specification](artifact/SPEC.md)
- [Reader test](artifact/references/reader-test.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review findings and optional inline document edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify the target document only when editing is requested or approved.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
