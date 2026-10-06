## Description:

Connects an agent to Google Calendar and Google Meet to manage events, invitations, meeting spaces, and call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams use this skill through an agent to schedule and manage Google Calendar events, respond to invitations, and manage Google Meet spaces and call history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar and Meet access can expose private events, attendee information, and meeting history.

Mitigation: Use a dedicated Google account or least-privilege OAuth scopes where possible; review the full tool list before installing.

Risk: Delete-calendar, out-of-office auto-decline, move, and meeting-management tools can make disruptive changes.

Mitigation: Confirm the target and intended change before high-impact actions; set GOG_READONLY=1 when only read access is needed.

Risk: Auth setup, Zoom credential storage, and general run tools extend access beyond basic calendar operations.

Mitigation: Avoid supplying Zoom S2S credentials unless meeting attachment is needed, and limit access to credential and escape-hatch tools.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text or JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can contain event, attendee, and meeting details.]

## Skill Version(s):

4.6.3 (source: server release, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
