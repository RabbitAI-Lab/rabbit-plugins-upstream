## Description:

Organizes Amazon review quality, packaging, and instruction issues into supplier feedback points, supporting evidence, and acceptance questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators and supplier-management teams use this skill to turn Amazon review samples into a supplier feedback checklist after checking available data and confirming any paid ARI operation. It is not intended to contact suppliers, place purchase orders, make contract decisions, or assign legal responsibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports broader operations capability than the advertised supplier-feedback-only scope.

Mitigation: Run only the documented supplier-feedback operations, verify that the quote and requestId match the intended product/supplier job before using --confirm, and prefer a publisher release that locks workflow and focus to product/supplier.

Risk: The workflow requires an ARI API key and may expose account, balance, product, review, and paid-action data to the ARI service.

Mitigation: Install only if that data sharing is acceptable, keep the API key scoped and protected, and confirm paid actions only after reviewing the quote.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/supplier-feedback)
- [README](artifact/README.md)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and text responses with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis actions require a quote and explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: server release metadata, artifact _meta.json, CHANGELOG, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
