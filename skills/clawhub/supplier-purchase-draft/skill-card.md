## Description:

Combines prepare supplier purchasing terms with create a purchase draft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement employees use this skill to read supplier CSV rows into purchasing terms and create purchase drafts for sourcing and renewal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated purchase drafts can affect procurement workflows if used without review.

Mitigation: Review generated drafts before relying on, submitting, or routing them into purchasing processes.

Risk: Supplier CSV data may contain business-sensitive supplier terms.

Mitigation: Use only supplier-term data that was intended to be provided to the agent and follow internal data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Supplier purchasing terms and purchase draft identifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces purchase_terms from supplier_csv and purchase_draft_id from purchase_terms.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
