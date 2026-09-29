## Description:

Connects an agent to Google Calendar and Google Meet to manage events, invitations, meeting spaces, and call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and teams use this skill through an agent to schedule and manage Google Calendar events, respond to invitations, and manage Google Meet spaces and call information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar and Meet access may allow broader account actions than expected.

Mitigation: Review tool permissions before installation; use a dedicated Google account or set GOG_READONLY=1 when only read access is needed.

Risk: Ending a Meet conference can disrupt participants without an enforced confirmation step.

Mitigation: Require explicit user approval before calling gog_meet_end.

Risk: Calendar deletion, unsubscribing, and unrestricted run tools can make high-impact account changes.

Mitigation: Restrict these tools to trusted, approval-gated workflows; configure Zoom credentials only when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [MCP tool responses with calendar and meeting information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event details, meeting codes, participant lists, and call history.]

## Skill Version(s):

4.5.2 (source: server-resolved release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
