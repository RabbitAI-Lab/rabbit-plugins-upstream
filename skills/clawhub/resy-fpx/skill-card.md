## Description:

Helps agents search Resy venues and availability, manage reservations, favorites, and Priority Notify through shell commands, and obtain a session token when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Resy account holders and developers use this skill to find restaurant tables and manage bookings, cancellations, favorites, and Priority Notify directly from a shell without the Resy MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booking, cancellation, favorites, and Priority Notify commands can change a real account without a built-in confirmation or dry-run step.

Mitigation: Read back the exact venue, date, time, party size, and payment details; require explicit confirmation before each write and verify the result afterward.

Risk: Browser-token setup connects a local profile to a signed-in Resy session.

Mitigation: Use browser pairing only if the account holder is comfortable linking that local profile to their signed-in session.

## Reference(s):

- [Resy API request examples](artifact/references/resy-api.md)
- [resy-fpx on ClawHub](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes requests for Resy account operations; write requests can change real reservations and subscriptions.]

## Skill Version(s):

1.3.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
