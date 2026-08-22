## Description:

Prepare supplier purchasing terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement operations users use this skill to convert supplied supplier terms data into concise purchase terms for a handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier input may include unnecessary sensitive supplier data beyond the fields needed for purchase terms.

Mitigation: Provide only the required supplier_id, currency, lead_days, incoterm, and renewal_month fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft-identifier)
- [Publisher profile: wxt-ai](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [Structured purchase_terms object with supplier_id, currency, lead_days, incoterm, and renewal_month.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses supplier_csv supplied in the current request and does not require credentials or private file access.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
