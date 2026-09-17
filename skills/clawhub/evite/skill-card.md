## Description:

This skill should be used when the user asks about Evite events or invitations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with Evite access can inspect invitations and hosted events, review guest lists and RSVP totals, RSVP to events, message guests, and create or update event invitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup runs an unpinned npm MCP server, which can change between installs.

Mitigation: Review the package before installation and pin a known version instead of relying on an unqualified npx resolution.

Risk: The skill can require Evite account passwords or session cookies for access.

Mitigation: Use a secret manager or runtime credential injection, and do not commit `.mcp.json` files containing credentials.

Risk: Browser-session cookie bootstrap may expose signed-in Evite sessions when enabled.

Mitigation: Set `EVITE_DISABLE_FETCHPROXY=1` unless browser-session cookie bootstrap is deliberately needed.

Risk: Connected tools can read and modify invitations, guest lists, RSVPs, messages, and events.

Mitigation: Inspect dry-run previews and require explicit `confirm: true` only after verifying the intended event action.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup guidance and dry-run previews for write actions when confirm is not true.]

## Skill Version(s):

0.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
