## Description:

Creates a local purchase draft from supplied supplier terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement staff use this skill to turn supplied purchasing terms into a draft record for sourcing or renewal work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operation writes a local purchase draft database that may be mistaken for an approved business record.

Mitigation: Use a dedicated output directory and review the draft before treating it as a business record.

## Reference(s):

- [Purchase Draft Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON purchase draft result and effect receipt; local SQLite draft record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a draft ID, status, supplier ID, and summary; does not place an order or confirm an external business action.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
