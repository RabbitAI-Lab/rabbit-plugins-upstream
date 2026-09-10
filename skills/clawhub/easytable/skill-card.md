## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget). Covers listing booking areas, dates and times, looking up existing bookings by phone, and creating/modifying/cancelling reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check restaurant booking availability and manage easyTable reservations through a user's own browser session. It supports listing booking areas, dates, and times, then creating, modifying, or cancelling reservations after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a privileged browser bridge with browser-context access.

Mitigation: Install only if the fetchproxy extension is trusted, and prefer a dedicated Chrome profile or an EasyTable-only tab.

Risk: Reservation lookup, modification, and cancellation can affect real bookings.

Mitigation: Do not look up, change, or cancel a reservation unless the requester proves they control the phone number or reservation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions]

**Output Format:** [Markdown with tool-use guidance and confirmation requirements]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reservation create, modify, and cancel actions are confirm-gated before execution.]

## Skill Version(s):

0.4.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
