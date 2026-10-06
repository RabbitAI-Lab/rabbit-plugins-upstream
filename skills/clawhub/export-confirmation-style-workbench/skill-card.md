## Description:

Create a delivery acknowledgement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agents handling routine deliveries use this skill to create an acknowledgement and record a receipt after delivery completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send acknowledgement data to an external destination using ambient settings.

Mitigation: For local-only use, remove the delivery endpoint and credentials; review any configured destination before running.

## Reference(s):

- [Delivery Receipt Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/export-confirmation-style-workbench)
- [Publisher profile: wxt-ai](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON confirmation result and local receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operation ID, confirmation status and receipt-created flag; configured delivery may return a delivery receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
