## Description:

Discover restaurants on Tock (exploretock.com) via MCP by listing cities, searching a metro, and retrieving venue details, bookable experiences, prices, party sizes, and open dates or times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover Tock restaurants, inspect availability and experiences, and check signed-in profile or reservation information through a read-only MCP workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP package and browser extension can read Tock pages visible in a signed-in browser tab, including profile and reservation history.

Mitigation: Install only when that access is acceptable, review the package and extension trust boundary, and keep signed-in browser access limited to intended use.

Risk: The skill reports Tock availability and account information but does not perform booking, payment, or cancellation.

Mitigation: Complete booking, payment, and cancellation directly on Tock, and treat the skill output as read-only guidance.

Risk: Reservation confirmation can be misleading if based only on a success screen or an immediate single reservation-history check.

Mitigation: Confirm bookings only when a confirmation artifact is captured and the reservation appears in a later reservation-history re-query.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp project link](https://github.com/chrischall/tock-mcp)
- [fetchproxy extension project link](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only Tock discovery, availability, profile, and reservation guidance through MCP tools.]

## Skill Version(s):

0.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
