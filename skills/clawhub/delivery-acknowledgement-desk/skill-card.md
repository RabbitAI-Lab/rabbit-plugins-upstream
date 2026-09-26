## Description:

Derive acknowledgement rules and create delivery receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and agents use this skill to set delivery acknowledgement guidance from a delivery profile and create a concise acknowledgement receipt from that guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be invoked when the user did not intend to set delivery acknowledgement guidance or create a receipt.

Mitigation: Invoke it only for explicit delivery acknowledgement tasks and review the generated guidance or receipt before using it in an operational workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/delivery-acknowledgement-desk)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [String or JSON object in the requested output field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces acknowledgement_guidance as a string and confirmation_result as an object with operation_id, confirmation_status, and receipt_created.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
