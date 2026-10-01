## Description:

Prepare supplier purchasing terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams use this skill to normalize supplier terms provided in a request for a purchasing handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unnecessary supplier information could be included in the supplied terms.

Mitigation: Provide only the supplier table data needed for the task; do not provide credentials or private files.

Risk: Normalized terms could be mistaken for a completed purchasing action.

Mitigation: Review the returned terms before handoff; the skill does not create or confirm a purchase.

## Reference(s):

- [Supplier Terms Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object containing purchase_terms]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes supplier ID, currency, lead time in days, Incoterm, and renewal month; does not persist a business artifact.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
