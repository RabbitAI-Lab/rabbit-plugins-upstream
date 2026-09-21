## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through an easyTable widget, including listing booking areas, dates, times, and existing bookings by phone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect easyTable restaurant availability and manage table reservations through the user's own browser session after pairing the fetchproxy extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a browser bridge and the user's active browser session to read availability and manage bookings.

Mitigation: Verify the fetchproxy extension source and approve pairing only for the booking tab the user intends to use.

Risk: Creating, modifying, or canceling a reservation can change a real booking using the name and mobile number supplied by the user.

Mitigation: Review the dry-run preview and set confirm:true only after verifying the restaurant, booking details, name, and mobile number.

Risk: Create and modify actions depend on a single-use Cloudflare Turnstile token from the loaded widget tab.

Mitigation: Keep the intended easyTable widget tab open and reload it before retrying if a token-related create or modify action fails.

## Reference(s):

- [easytable ClawHub listing](https://clawhub.ai/chrischall/skills/easytable)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Text guidance with structured tool-call parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reservation-changing actions are dry-run previews until the user confirms with confirm:true.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
