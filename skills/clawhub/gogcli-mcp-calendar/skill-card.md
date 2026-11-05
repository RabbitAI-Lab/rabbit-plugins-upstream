## Description:

Use when the user asks to manage Google Calendar events or Google Meet spaces. Triggers for scheduling, listing events, creating/updating/deleting events, responding to invitations, creating Meet spaces, ending conferences, listing meeting participants or call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People use this skill to view and manage Google Calendar events and to create, configure, and review Google Meet spaces and calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some event moves may not request confirmation, and deleting a calendar can remove all its events.

Mitigation: Require user approval before organizer-changing moves and calendar deletion; begin with GOG_READONLY=1 when write access is not needed.

Risk: Zoom setup can expose credentials through local process inspection.

Mitigation: Avoid the Zoom setup tool until credentials can be supplied without command-line exposure.

Risk: The external gog executable and future downloaded releases were not validated by the review.

Mitigation: Pin the package version, use a trusted gog executable, and protect its persistent credential store.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [Project repository](https://github.com/chrischall/gogcli-mcp)
- [gogcli dependency](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [API Calls, Guidance]

**Output Format:** [Structured Google Calendar and Meet tool calls and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, modify, or delete calendar data and change Meet settings.]

## Skill Version(s):

4.9.1 (source: server release evidence, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
