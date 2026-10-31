## Description:

Check easyTable restaurant availability, look up bookings by phone, and cancel bookings from a shell with the fpx CLI using a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users who want to check easyTable restaurant availability, find an existing booking by phone number, or manage a reservation from shell scripts using their paired browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reservation changes affect a real restaurant booking.

Mitigation: Verify the restaurant and booking details before authorizing a change; do not use live create or cancel calls for testing.

Risk: Booking lookup and management can involve guest contact details.

Mitigation: Share only the guest details needed for the requested action.

Risk: Requests use a paired browser extension with site access to easytable.com.

Mitigation: Check the CLI and extension sources, limit browser site access to easytable.com, and revoke pairing when it is no longer needed.

## Reference(s):

- [easytable-requests.md](references/easytable-requests.md)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [easyTable booking widget](https://book.easytable.com/book/)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and HTML or JSONP response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests use restaurant, booking-area, language, party-size, date, and time values as applicable.]

## Skill Version(s):

1.2.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
