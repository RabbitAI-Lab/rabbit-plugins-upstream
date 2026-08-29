## Description:

Query Tock restaurant discovery, availability, venue calendar, and signed-in reservation data from a shell through the fpx CLI and a user-approved browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover Tock metros and restaurants, inspect venue availability, and retrieve the signed-in user's reservations through read-only shell commands. It is useful when Tock data is needed in scripts or environments where the Tock MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a user-approved browser bridge to make read-only requests through an exploretock.com session.

Mitigation: Install and run it only when that browser-session access is acceptable for the intended environment.

Risk: Reservation and profile examples can expose names, email addresses, and reservation history in terminal output or temporary files.

Mitigation: Avoid shared machines for these commands and delete generated temporary files after use.

Risk: The skill cannot book or cancel reservations and a post-booking screen alone is not proof of confirmation.

Mitigation: Complete booking or cancellation on exploretock.com and verify confirmed bookings through a confirmation ID, URL, email, and a later PatronReservationHistory re-query.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [requests.md](references/requests.md)
- [extract-redux-slice.mjs](references/extract-redux-slice.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, jq recipes, JSON request bodies, and a JavaScript helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only and may include restaurant listings, availability data, reservation records, and account identity fields returned by Tock.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
