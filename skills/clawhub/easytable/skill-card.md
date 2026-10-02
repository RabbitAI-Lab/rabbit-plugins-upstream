## Description:

Helps users check easyTable restaurant availability and create, change, or cancel table reservations through their browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Diners use this skill to check restaurant booking areas, dates, and times, and to make, find, change, or cancel easyTable reservations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The booking flow requires a browser extension with access to the user's booking session.

Mitigation: Confirm the ContextMint Bridge extension source is trusted before installing or pairing it.

Risk: Booking actions handle guest names and mobile numbers and may create, change, or cancel reservations.

Mitigation: Share contact details only when needed and approve changes only after checking the reservation preview against the request.

Risk: An uncertain booking response can leave a reservation already created, and a modification can clear existing details.

Mitigation: Look up the reservation before retrying; confirm any existing email, comments, and company details before modifying it.

## Reference(s):

- [easytable on ClawHub](https://clawhub.ai/chrischall/skills/easytable)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with availability details, booking results, and confirmation previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reservation changes require user confirmation.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
