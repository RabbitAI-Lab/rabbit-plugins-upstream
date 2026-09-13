## Description:

Query Tock restaurant discovery, venue availability, and signed-in user reservations from shell commands through the fpx CLI and a user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Tock metros, restaurants, venue calendars, availability, and the signed-in user's reservations without running a MCP server. It is suited for read-only lookup and scripting workflows, not booking or cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-session bridge access may expose the signed-in user's Tock session and reservation context.

Mitigation: Use the skill only with the signed-in account holder's consent, pin and verify the fpx and extension source, and restrict browser site access to Tock.

Risk: Reservation commands can output names, emails, reservation IDs, dates, and party details to local files.

Mitigation: Avoid shared temporary paths for reservation responses, and delete or redact files that contain reservation or identity data.

Risk: The skill cannot book or cancel reservations and may only verify bookings made outside the skill after reservation history refreshes.

Mitigation: Use Tock directly for booking or cancellation, and treat outside bookings as confirmed only after a confirmation artifact and a later reservation-history re-query.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Skill instructions](artifact/SKILL.md)
- [Tock request recipes](artifact/references/requests.md)
- [Redux slice extractor](artifact/references/extract-redux-slice.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, jq filters, JavaScript helper usage, and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Tock reservation identity data when the browser tab is signed in; users should avoid writing that data to shared temporary files.]

## Skill Version(s):

0.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
