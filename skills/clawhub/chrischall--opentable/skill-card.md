## Description:

Manage OpenTable reservations through MCP by searching restaurants, checking slot availability, booking tables, listing or canceling reservations, modifying reservations, and managing favorites through a signed-in OpenTable browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage OpenTable restaurant discovery, availability checks, reservations, cancellations, modifications, and favorites. It is intended for users who have installed the required MCP server and browser extension and are signed in to OpenTable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can book, modify, cancel, or favorite real OpenTable reservations using the user's signed-in browser session.

Mitigation: Require explicit user confirmation before any booking, modification, favorite change, or cancellation.

Risk: Reservation actions may involve cancellation policies, no-show fees, or card holds.

Mitigation: Before committing an action, show the restaurant, date, time, party size, cancellation or no-show policy, and any card hold details.

Risk: The skill depends on an active signed-in browser session.

Mitigation: Install and run it only when the user is comfortable letting an agent use that OpenTable session.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce booking, modification, cancellation, favorite-management, and setup guidance for MCP tool use.]

## Skill Version(s):

0.16.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
