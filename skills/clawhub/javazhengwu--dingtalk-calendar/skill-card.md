## Description:

Helps an agent use mcporter to connect to DingTalk calendar and contacts MCP services for calendar management, availability checks, and meeting room booking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[javazhengwu](https://clawhub.ai/user/javazhengwu)

### License/Terms of Use:

MIT

## Use Case:

Developers and employees use this skill to configure DingTalk calendar and contacts MCP services, then have an agent propose mcporter commands for creating, listing, updating, and deleting events, checking coworker availability, searching contacts, and booking meeting rooms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose coworker availability and contact details through DingTalk MCP services.

Mitigation: Require explicit user confirmation before querying another person's availability or contact details, and limit queries to the minimum users and time range needed.

Risk: The skill includes commands that can update or delete calendar events.

Mitigation: Review the target event ID and full command arguments with the user before executing any update or deletion.

Risk: The documented setup uses an unpinned global mcporter CLI install.

Mitigation: Install mcporter only from a trusted source and prefer a pinned or local install when operating in managed environments.

## Reference(s):

- [DingTalk MCP Marketplace](https://mcp.dingtalk.com)
- [ClawHub skill page](https://clawhub.ai/javazhengwu/skills/dingtalk-calendar)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended for manual review and execution against configured DingTalk MCP endpoints.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; artifact package.json and CHANGELOG list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
