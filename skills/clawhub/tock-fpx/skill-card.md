## Description:

Query Tock restaurant discovery, availability, venue details, and the signed-in user's reservations from a shell with the fpx CLI through the user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to query Tock data from shell workflows without running the tock-mcp server. It supports read-only restaurant discovery, metro and venue lookup, availability inspection, and user-directed reservation or account-identity reads through an existing browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in reservation and account-identity commands can expose personal names, email addresses, and reservation details from the user's Tock account.

Mitigation: Run those commands only when the user explicitly wants that information retrieved, and avoid storing or sharing the returned personal data unnecessarily.

Risk: The skill depends on a paired fpx/Transporter bridge and an exploretock.com browser tab, so results can fail or be incomplete when the tab is not signed in, not challenge-cleared, or not connected.

Mitigation: Check bridge health and login state before relying on results, and treat failed or empty signed-in reads as inconclusive unless the command output confirms the condition.

Risk: Booking and cancellation are out of scope, and external booking attempts can be difficult to verify immediately from Tock's delayed reservation backend.

Mitigation: Use the skill only for read-only queries, and treat bookings as confirmed only after a confirmation ID, URL, or email is captured and a later reservation-history query verifies the reservation.

## Reference(s):

- [Tock requests for fpx](references/requests.md)
- [extract-redux-slice.mjs](references/extract-redux-slice.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, jq filters, JSON request bodies, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow guidance; signed-in reservation and account-identity queries may return personal data from the user's Tock account.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
