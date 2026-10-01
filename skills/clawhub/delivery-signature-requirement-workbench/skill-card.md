## Description:

Compose a delivery signature section.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations teams use this skill to compose a signature-requirement section for a delivery handoff document and save a local documentation record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill writes a delivery documentation record to the selected local output directory.

Mitigation: Choose a dedicated output directory and review the generated receipt path and record.

Risk: A local delivery record could be mistaken for confirmation that a recipient signed or a handoff occurred.

Mitigation: Verify signatures and delivery status through the appropriate external business process.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/delivery-signature-requirement-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response and local JSON documentation record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response includes a local artifact receipt; it does not confirm an external delivery or signature.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
