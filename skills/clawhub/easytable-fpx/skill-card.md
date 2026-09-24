## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI, including listing booking areas, dates, and times, looking up bookings by phone, and cancelling bookings through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide an agent through EasyTable availability checks and booking-management commands when they need browser-backed access from a shell instead of a running MCP server. It is intended for authorized reservation workflows where the restaurant, customer phone number, date, time, and booking id can be confirmed before any write action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live write commands can cancel, create, or modify real restaurant bookings.

Mitigation: Use write commands only for authorized reservations, and confirm the restaurant, customer, date, time, phone number, and booking id before submitting any cancel, create, or modify request.

Risk: Booking lookups and reservation payloads can expose phone numbers and booking details.

Mitigation: Treat phone numbers and reservation details as personal data and avoid sharing command output beyond the authorized workflow.

Risk: Testing live write endpoints can unintentionally alter real bookings.

Mitigation: Do not use live create, cancel, or modify calls merely to test the flow; prefer read-only availability checks unless a real authorized booking action is intended.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return HTML fragments or JSONP responses that require parsing before acting on results.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
