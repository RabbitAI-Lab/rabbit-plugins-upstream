## Description:

Queries Tock for restaurant discovery, venue availability, and the signed-in user's reservations through the fpx CLI and a browser tab without running the tock-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Tock users use this skill to find restaurants, inspect bookable dates and times, and view their own reservations from a shell without an MCP server. The skill does not book or cancel reservations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reservation responses can expose names, email addresses, reservation IDs, venues, and dates.

Mitigation: Treat reservation results as private; avoid saving them in shared temporary directories and remove saved responses when finished.

Risk: Queries run through fpx and the ContextMint Bridge extension using a browser session with access to exploretock.com.

Mitigation: Install and pair the extension only if you are comfortable with read-only requests to exploretock.com from that session.

## Reference(s):

- [Tock fpx request recipes](references/requests.md)
- [Redux slice extraction helper](references/extract-redux-slice.mjs)
- [ContextMint Bridge source and installation](https://github.com/nullnet-app/contextmint-bridge)
- [Tock](https://www.exploretock.com)
- [tock-fpx release](https://clawhub.ai/chrischall/skills/tock-fpx)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and structured JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; reservation results may contain personal information.]

## Skill Version(s):

1.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
