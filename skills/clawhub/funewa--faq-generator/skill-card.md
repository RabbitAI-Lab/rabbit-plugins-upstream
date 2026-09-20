## Description:

Generates suggested FAQ topics and evidence-backed draft answers for Amazon product pages from repeated review questions and product fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to identify FAQ themes for Amazon listings, check available review and product evidence, and generate FAQ suggestions after reviewing a quote. It is not intended for customer-service automation, legal or policy review, or automatic listing publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reports that the skill can run broader server-defined product-operation workflows than its fixed FAQ purpose promises.

Mitigation: Review the skill before installing when strict FAQ-only behavior is required, and only confirm paid operations when the quote clearly matches the intended listing/faq task.

Risk: Paid collection or analysis can spend account credits.

Mitigation: Use the quoted requestId flow and require explicit user confirmation before running paid operations.

Risk: The skill stores or reads an ARI API key for authenticated service access.

Mitigation: Use the official ARI service endpoint, protect the local key, and avoid passing custom workflow or focus values.

## Reference(s):

- [Amazon Product FAQ Operation Workflow](references/operation-workflow.md)
- [Amazon Product FAQ API Reference](references/reference.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/faq-generator)
- [Publisher profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and service-returned analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid operations must be quoted first and explicitly confirmed by the user.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, CHANGELOG, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
