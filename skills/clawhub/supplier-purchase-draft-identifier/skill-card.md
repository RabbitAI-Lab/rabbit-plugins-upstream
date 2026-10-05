## Description:

Prepare supplier purchasing terms from a supplied CSV row or structured record.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams use this skill to normalize supplier purchasing terms for a handoff from a supplied CSV row or record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier terms supplied to a local script may contain sensitive business information.

Mitigation: Use a dedicated input file with only the terms needed for the request.

Risk: Changing the bundled role or configuration may enable downstream output-directory behavior.

Mitigation: Review downstream behavior separately before changing the shipped configuration.

## Reference(s):

- [Supplier Terms Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns purchase_terms with supplier_id, currency, lead_days, incoterm, and renewal_month; shipped configuration does not persist data or use the network.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
