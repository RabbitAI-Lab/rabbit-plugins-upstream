## Description:

Helps users find restaurants, book and cancel Resy reservations, manage favorites, and subscribe to availability notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy users can search restaurant availability, review and confirm bookings or cancellations, and manage favorite venues and availability alerts through an assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resy account credentials stored in assistant configuration could be exposed.

Mitigation: Use user-local configuration and keep files containing the Resy password out of version control and shared folders.

Risk: Booking or cancellation could commit to an unintended slot or fee.

Mitigation: Review the venue, time, seating, terms, and any fees in the preview before confirming.

Risk: Resy's unofficial private API may change or stop working.

Mitigation: Check availability and transaction results before relying on them; reassess the integration if Resy changes its web app.

## Reference(s):

- [Resy skill listing](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with restaurant availability, reservation details, and confirmation previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and cancellation require user confirmation.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
