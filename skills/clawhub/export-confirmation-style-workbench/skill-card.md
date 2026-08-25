## Description:

Create a delivery acknowledgement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and business users use this skill to turn supplied delivery-session guidance into a concise delivery acknowledgement receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated acknowledgements could be mistaken for finalized business records.

Mitigation: Review the generated acknowledgement before storing it or treating it as an official business record.

Risk: Incomplete or ambiguous acknowledgement guidance can produce an incomplete receipt.

Mitigation: Provide complete acknowledgement guidance and confirm the operation_id, confirmation_status, and receipt_created values before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/export-confirmation-style-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON-compatible object with operation_id, confirmation_status, and receipt_created fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns confirmation_result from supplied acknowledgement_guidance; no credentials or private-file access required.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
