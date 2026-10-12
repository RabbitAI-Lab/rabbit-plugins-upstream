## Description:

Helps agents manage Google Calendar events and Google Meet spaces, including scheduling, invitations, meeting history, and conference controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams use this connector through an agent to organize Google Calendar events, respond to invitations, and manage Google Meet spaces and calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can use and persist Google account credentials and offers Zoom credential setup.

Mitigation: Install only in a trusted environment; avoid shared high-privilege accounts and require explicit approval before storing Zoom credentials.

Risk: Tools can read calendar sharing details and delete calendars or unsubscribe from them.

Mitigation: Review the full tool list and prefer GOG_READONLY when write access is unnecessary.

Risk: Meeting controls can end an active conference.

Mitigation: Require explicit human approval before ending meetings.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain event details, participant information, meeting links, or action confirmations.]

## Skill Version(s):

4.8.0 (source: ClawHub release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
