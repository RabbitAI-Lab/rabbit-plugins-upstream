## Description:

Helps an agent manage Google Calendar events and Google Meet spaces, including scheduling, invitations, and meeting history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People using an agent to organize Google Calendar events and Google Meet spaces can look up availability, schedule or change events, respond to invitations, and manage meetings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes account authorization and broader calendar administration than its brief description suggests.

Mitigation: Review tool permissions before installation, especially on shared or hosted agents; use GOG_READONLY=1 when only reading is needed.

Risk: Deleting events or calendars and ending active meetings can disrupt others.

Mitigation: Require explicit user approval before calendar deletion, meeting termination, or other high-impact changes.

Risk: Auth and calendar command tools can perform actions beyond the dedicated scheduling tools.

Mitigation: Manually control auth-run and calendar-run tools and limit access to trusted users.

Risk: Optional Zoom attachment support may require additional credentials.

Mitigation: Do not supply Zoom credentials unless Zoom attachment support is needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [MCP tool responses containing calendar and meeting information or action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated gogcli account; available actions depend on account permissions.]

## Skill Version(s):

4.6.0 (source: server release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
