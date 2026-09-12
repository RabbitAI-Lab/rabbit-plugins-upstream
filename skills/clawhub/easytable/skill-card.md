## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget). Covers listing booking areas, dates and times, looking up existing bookings by phone, and creating/modifying/cancelling reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to work through easyTable restaurant booking widgets: checking areas, dates, and times, then creating, modifying, finding, or canceling reservations in the user's browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on an unpinned browser extension that bridges into an active browser tab.

Mitigation: Review the fetchproxy extension before installing it, prefer a pinned reviewed version, and use it in a dedicated browser profile or tab for easyTable bookings.

Risk: Reservation actions handle personal booking data and can create, modify, or cancel real bookings.

Mitigation: Confirm create, modify, or cancel actions only after checking the restaurant, date, time, party size, name, and phone number shown in the preview.

## Reference(s):

- [ClawHub easytable skill page](https://clawhub.ai/chrischall/skills/easytable)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance with tool names, setup steps, booking workflow instructions, and confirmation requirements]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Create, modify, and cancel actions are confirmation-gated and return a dry-run preview before applying changes.]

## Skill Version(s):

0.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
