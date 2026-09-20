## Description:

Manage Resy restaurant reservations via MCP: search venues, book tables, list and cancel reservations, manage favorites, and subscribe to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Resy restaurant availability, reservations, favorites, and Priority Notify subscriptions through a configured Resy MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can book, cancel, favorite, or add notifications on a live Resy account.

Mitigation: Require confirmation showing the exact venue, date, time, party size, and action before any write action.

Risk: The MCP server requires a Resy email and password.

Mitigation: Install only in trusted agent environments and scope credential access to the Resy MCP server.

Risk: The server uses private Resy web-app endpoints that may change without notice.

Mitigation: Stop on unexpected failures or changed responses and ask the user to verify before retrying state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Resy credentials; write actions can change live reservations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
