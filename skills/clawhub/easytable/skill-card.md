## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget). Covers listing booking areas, dates and times, looking up existing bookings by phone, and creating/modifying/cancelling reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can check restaurant availability and manage reservations at restaurants that use easyTable. The skill looks up booking areas, dates, times, and existing reservations, and can create, change, or cancel a booking with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension connects the skill to the restaurant booking widget.

Mitigation: Verify the extension download and approve only the domains and capabilities needed for easyTable.

Risk: Creating, changing, or cancelling a reservation can affect a real booking.

Mitigation: Review the booking preview and confirm the requested change before it is submitted.

Risk: Changing a reservation replaces the booking and could clear details that cannot be read back, such as email or special requests.

Mitigation: Ask for the existing details and pass them through unchanged; clear them only when the user requests it.

## Reference(s):

- [easyTable booking widget](https://book.easytable.com/book/?id=%3CrestaurantId%3E)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with reservation details and confirmation previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include availability, booking details, or a preview requiring user approval before a reservation is changed.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
