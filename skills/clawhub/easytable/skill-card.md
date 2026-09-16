## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget). Covers listing booking areas, dates and times, looking up existing bookings by phone, and creating/modifying/cancelling reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect availability and manage reservations for restaurants that expose an easyTable booking widget. It supports listing booking areas, dates, and times, finding existing bookings by mobile number, and creating, modifying, or canceling reservations with confirmation for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an unpinned third-party browser bridge paired with a live easyTable booking tab.

Mitigation: Review the fetchproxy extension before installing, prefer a pinned or signed release if available, and restrict or disable the extension when not booking.

Risk: Reservation names, mobile numbers, booking IDs, and short-lived Turnstile tokens may pass through the browser bridge during booking operations.

Mitigation: Pair only with the intended easyTable tab and avoid sharing unnecessary personal details beyond the booking workflow.

Risk: Create, modify, and cancel operations can change real reservations.

Mitigation: Use the built-in dry-run behavior and require explicit confirmation before applying write actions.

## Reference(s):

- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [easyTable booking widget](https://book.easytable.com/book/?id=<restaurantId>)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, setup steps, and booking-flow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are confirmation-gated; booking flows may involve reservation names, mobile numbers, booking IDs, and short-lived Turnstile tokens.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
