## Description:

Manage OpenTable restaurant reservations through an MCP server, including restaurant search, availability checks, booking, reservation listing and canceling, and favorites management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent find restaurants, check OpenTable availability, book or modify tables, cancel reservations, and manage saved restaurants through the user's signed-in OpenTable browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in OpenTable browser session to book, modify, or cancel reservations.

Mitigation: Require the agent to show the restaurant, date, time, party size, and action, then wait for explicit user confirmation before any account-changing call.

Risk: Some reservations may include cancellation policies, no-show fees, or saved-card holds.

Mitigation: Before booking or modifying, require preview output that surfaces policy and fee details and obtain explicit confirmation from the user.

Risk: Live slot tokens are short lived, so delayed decisions can cause stale or failed bookings.

Mitigation: Refresh availability immediately before booking when the user has taken time to decide.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP tool usage guidance for account-affecting OpenTable actions.]

## Skill Version(s):

0.16.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
