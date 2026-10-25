## Description:

Connects agents to Google Calendar and Google Meet to manage events, invitations, meeting spaces, and call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and agents use this connector to find, schedule, change, or cancel Google Calendar events and to create and manage Google Meet spaces and participation records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent Google Calendar and Meet credentials, and optional Zoom credentials, can expose account data if the host is shared or compromised.

Mitigation: Use a dedicated account, review OAuth scopes, and isolate the keyring and process environment; provide Zoom credentials only when needed.

Risk: Calendar changes and meeting administration can affect other people and shared resources.

Mitigation: Set GOG_READONLY=1 for read-only or shared use, and review permissions before enabling changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, Structured calendar and meeting data]

**Output Format:** [MCP tool responses, including text and structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain event, attendee, meeting, and account details.]

## Skill Version(s):

4.8.1 (source: ClawHub release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
