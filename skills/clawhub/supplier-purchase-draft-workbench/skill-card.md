## Description:

Create a purchase draft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement operations users use this skill to turn supplied supplier purchase terms into a concise purchase draft result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated purchase draft reflects the supplier terms supplied by the user, so inaccurate or incomplete terms can lead to an incorrect draft result.

Mitigation: Review supplier terms before relying on the generated purchase draft result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft-workbench)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON object with draft_id, status, supplier_id, and summary fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the purchase_draft_id field from user-supplied purchase_terms.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
