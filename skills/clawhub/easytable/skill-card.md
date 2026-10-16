## Description:

Helps users check restaurant availability and create, change, or cancel easyTable reservations through their browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant guests use this skill to find available tables and manage their own easyTable bookings, including confirming reservation changes before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The booking flow uses an active browser session through the ContextMint Bridge extension.

Mitigation: Install and use the extension only if comfortable granting it access to the active easyTable tab.

Risk: Creating, modifying, or cancelling a reservation changes a real booking; modification can clear email, company, or comment fields.

Mitigation: Check each confirmation preview and preserve existing fields unless intentionally clearing them.

## Reference(s):

- [easytable skill on ClawHub](https://clawhub.ai/chrischall/skills/easytable)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with availability, booking details, and confirmation previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reservation changes require user confirmation.]

## Skill Version(s):

1.2.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
