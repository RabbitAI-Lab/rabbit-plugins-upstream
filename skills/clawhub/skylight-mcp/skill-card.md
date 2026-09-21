## Description:

Connects agents to a signed-in Skylight Calendar account so they can read and manage family calendar events, chores, shared lists, meal plans, messages, photos, and frame settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate a Skylight family hub through a configured MCP server. It supports calendar, chore, shared-list, meal, message, photo, frame, device, and member workflows for the user's own signed-in Skylight account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector requires storing Skylight email and password credentials in MCP configuration.

Mitigation: Prefer project-local configuration, restrict access to the config file, and install only after reviewing the npm or source package.

Risk: The connector has broad read and write access to shared family hub data, including potentially privacy-sensitive calendar, message, photo, member, device, and list content.

Mitigation: Manually confirm destructive or privacy-sensitive actions such as deletes, uploads, member or device changes, and message or photo operations.

Risk: Some recurrence-scoped updates or deletes can affect events or chores beyond the named occurrence.

Mitigation: Respect the documented dry-run confirmation gates and do not report a gated change as completed until the same call is reissued with confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight](https://www.ourskylight.com)
- [Source link listed in skill documentation](https://github.com/chrischall/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration examples, inline shell commands, and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose MCP tool calls that read or modify shared family hub data; some recurrence-scoped writes require explicit confirmation.]

## Skill Version(s):

1.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
