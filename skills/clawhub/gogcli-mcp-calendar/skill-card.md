## Description:

Helps agents manage Google Calendar events and Google Meet spaces, including invitations, meeting history, and participants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent with Google Calendar and Meet access can schedule and manage events, respond to invitations, configure meeting spaces, and review call activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can end a live Google Meet conference without enforced confirmation.

Mitigation: Avoid shared or highly autonomous use until ending a conference requires explicit confirmation.

Risk: Access to Google Calendar and Meet can expose meeting details or change events.

Mitigation: Grant access only to intended accounts and prefer GOG_READONLY=1 for read-only tasks.

Risk: Broad file access or optional Zoom credentials expand the data available to the agent.

Mitigation: Keep GOG_FILE_ROOTS narrowly scoped, never set it to /, and provide Zoom credentials only when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [MCP tool responses with calendar and meeting details or operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected accounts and granted permissions.]

## Skill Version(s):

4.7.1 (source: server-resolved release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
