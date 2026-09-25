## Description:

This skill should be used when the user asks about Apple app data via the native Swift MCP - Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, or Photos on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users on macOS use this skill to let an agent read, search, create, update, send, export, or delete data in native Apple apps through a Swift MCP server with separated read and write tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access private local Apple app data after macOS permissions are granted.

Mitigation: Install only when this access is intended, review macOS TCC prompts carefully, and grant Full Disk Access or Automation access only when the task requires it.

Risk: Write, send, delete, export, and import tools can modify local Apple app data or communicate externally.

Mitigation: Start with read-only tools where possible and approve write-capable tools only for specific tasks that need them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [GitHub project](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with tool usage, configuration, command, and code snippets as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only or write-capable MCP tool recommendations depending on the user's Apple app task and granted macOS permissions.]

## Skill Version(s):

2.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
