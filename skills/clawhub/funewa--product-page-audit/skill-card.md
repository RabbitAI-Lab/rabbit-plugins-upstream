## Description:

Audits a single Amazon product page by comparing the listing title, bullet points, images, and product details against real buyer review feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to review one Amazon product page, identify gaps between page claims and buyer experience, and receive evidence-based audit findings after an explicit paid-run confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can submit operation parameters outside the documented fixed audit/page workflow.

Mitigation: Use only the documented audit/page commands and avoid workflow, focus, competitor, or other out-of-scope options.

Risk: Paid analysis or collection can consume account credits.

Mitigation: Review the quote and proceed only after explicit user confirmation for the specific requestId.

Risk: The ARI API key is a credential.

Mitigation: Store it securely and avoid sharing setup output, error logs, or authorization-session details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-page-audit)
- [Operation Workflow](references/operation-workflow.md)
- [API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, evidence summaries, and CLI command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid analysis runs.]

## Skill Version(s):

1.4.11 (source: _meta.json, CHANGELOG, script constant, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
