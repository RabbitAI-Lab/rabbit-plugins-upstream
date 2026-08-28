## Description:

Evite lets an agent use the evite-mcp server to read and manage Evite invitations, guest lists, RSVP tallies, messages, and hosted events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to let an agent check Evite events, inspect guest lists and RSVP status, respond to invitations, message guests, and create or update hosted events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can read and change authenticated Evite account data.

Mitigation: Install it only when authenticated Evite access is acceptable for the intended agent workflow.

Risk: Copied raw session cookies can expose account access if mishandled.

Mitigation: Prefer environment-stored credentials over copied cookies, and disable fetchproxy when browser-session reuse is not desired.

Risk: Write actions can send messages, change guests, update RSVPs, or alter hosted events.

Mitigation: Review the dry-run preview before setting confirm:true for any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)
- [Evite website](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require confirm:true and otherwise return dry-run previews; authenticated Evite credentials or session cookies are required for live use.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
