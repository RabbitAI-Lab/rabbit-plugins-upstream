## Description:

Discover restaurants and Tock availability through MCP, including metros, venue details, bookable experiences, prices, party sizes, open times, profile details, and reservation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Tock restaurant discovery, availability, profile, and reservation status through an MCP server. It is useful for finding venues and times while leaving booking, cancellation, and payment on exploretock.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and fetchproxy extension can read Tock pages through the user's signed-in browser tab, including profile and reservation history for account tools.

Mitigation: Install only from trusted sources, review the MCP and extension before use, and use account tools only in a browser session you are comfortable exposing to the integration.

Risk: The skill reports availability and verification data but does not complete prepaid bookings, cancellations, or payments.

Mitigation: Complete booking actions directly on exploretock.com and treat any booking as confirmed only after both an external confirmation signal and a confirmed result from tock_verify_reservation.

## Reference(s):

- [tock-mcp package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp source](https://github.com/chrischall/tock-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include restaurant, availability, profile, reservation, healthcheck, and verification results returned by MCP tools.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
