## Description:

Use when the user asks to manage Google Calendar events or Google Meet spaces. Triggers for scheduling, listing events, creating/updating/deleting events, responding to invitations, creating Meet spaces, ending conferences, listing meeting participants or call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to view and manage Google Calendar events, check availability, respond to invitations, and manage Google Meet spaces and call information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event transfers may occur without confirmation.

Mitigation: Require approval for event transfers regardless of email settings.

Risk: Zoom credential setup can pass secrets through process arguments.

Mitigation: Avoid the Zoom credential-setup tool until secrets can be supplied without process arguments.

Risk: Calendar access can expose or change more data than needed.

Mitigation: Use a dedicated account with only required Google permissions; set GOG_READONLY=1 for lookup-only use and review whole-calendar deletion previews carefully.

## Reference(s):

- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Calendar and meeting data]

**Output Format:** [Structured tool results and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect the connected Google account and requested calendar or meeting operation.]

## Skill Version(s):

4.10.0 (source: server-resolved release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
