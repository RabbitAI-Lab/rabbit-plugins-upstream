## Description:

Add entries to a renewal schedule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agreement operations teams use this skill to add dated obligations to a renewal schedule and receive a schedule receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agreement IDs, clause IDs, and due dates may leave the local environment when delivery is configured.

Mitigation: Review sensitive inputs and keep delivery variables and configuration unset unless external submission is intended and the destination is trusted.

Risk: Locally saved schedule records may contain sensitive agreement information.

Mitigation: Use a controlled, access-restricted output directory and review stored artifacts before sharing them.

## Reference(s):

- [Renewal Schedule Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/agreement-renewal-schedule-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON schedule receipt and local CSV renewal schedule]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The receipt includes a schedule ID and rows; configured delivery also returns a delivery receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
