## Description:

Connects an agent to Google Calendar and Meet to manage events, invitations, meeting spaces, and call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams use this skill to view and manage Google Calendar events and invitations, and to create or manage Google Meet spaces through an authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ending a live Google Meet conference does not require a separate confirmation prompt.

Mitigation: Require explicit user approval before invoking gog_meet_end, and do not expose this action to untrusted agents.

Risk: Zoom credential tools can store credentials and contact Zoom, beyond the primary Google Calendar and Meet use case.

Mitigation: Enable Zoom credential tools and Zoom network access only if needed; review their permissions and credential handling first.

Risk: An agent with account access can change calendar events and meeting settings.

Mitigation: Connect only a trusted agent to the intended Google account; set GOG_READONLY=1 when changes are unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event details, meeting information, and action results.]

## Skill Version(s):

4.7.0 (source: server-resolved release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
