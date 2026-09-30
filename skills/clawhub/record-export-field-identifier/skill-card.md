## Description:

Extracts and normalizes ACCT-style account references from supplied customer record notes into a structured record field.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Customer reporting staff use this skill to prepare a normalized account-reference field from customer record notes supplied in a request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account references in customer notes may be business-sensitive.

Mitigation: Limit access to supplied notes and review the extracted field before reuse.

Risk: Broad field-preparation wording may obscure that the operation requires an ACCT-style account reference.

Mitigation: Confirm the input contains the expected account reference and check the result against the source note.

## Reference(s):

- [Customer Record Field Prep on ClawHub](https://clawhub.ai/wxt-ai/skills/record-export-field-identifier)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [JSON object with a record_field containing record_id, field_name, and field_value]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normalizes an ACCT-style reference; does not persist a business artifact.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
