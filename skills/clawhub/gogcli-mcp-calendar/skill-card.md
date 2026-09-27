## Description:

Helps agents manage Google Calendar events and Google Meet spaces, including scheduling, invitations, meeting history, and participants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams use this skill through an agent to find and manage calendar events, respond to invitations, and create or manage Google Meet spaces and calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar changes and meeting actions can affect other people or disrupt active meetings, and some actions lack a separate confirmation step.

Mitigation: Review the requested action and its participants before proceeding; explicitly confirm destructive changes and ending an active conference.

Risk: Access to an important Google account exposes calendar data and permits high-impact actions.

Mitigation: Use a dedicated, least-privileged account where possible, and enable GOG_READONLY when only reading is needed.

Risk: Google and Zoom credentials may be stored on the host.

Mitigation: Review installation and credential permissions before use, and protect the host account and stored credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [MCP tool responses with text or structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include calendar details, meeting information, and participant data.]

## Skill Version(s):

4.5.1 (source: ClawHub release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
