## Description:

Query Tock restaurant discovery, venue availability, and signed-in user reservations from shell workflows using the fpx CLI and a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Tock metros, restaurants, venue calendars, availability, reservations, and account identity from command-line workflows. It is intended for read-only lookup and reporting, not booking or cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reservation and account identity commands can expose personal account details from a signed-in Tock browser session.

Mitigation: Treat reservation and profile outputs as personal data, avoid shared or logged terminals, and prefer public browsing commands unless signed-in details are intentionally needed.

Risk: Users may mistake a booking attempt made outside the skill for a confirmed reservation before Tock's reservation history reflects it.

Mitigation: Treat a booking as confirmed only after capturing a confirmation ID, URL, or email and verifying it appears in a later PatronReservationHistory query.

Risk: Bot challenges, bridge failures, or sign-in interstitials can produce non-JSON or error responses that look like transport success.

Mitigation: Check fpx exit codes, GraphQL errors, and response shape before parsing or reporting reservation data.

## Reference(s):

- [Tock requests for fpx](references/requests.md)
- [extract-redux-slice.mjs](references/extract-redux-slice.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, jq filters, JSON request bodies, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookup workflows; signed-in reservation and identity outputs can contain personal data.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
