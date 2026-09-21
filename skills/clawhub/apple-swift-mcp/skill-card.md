## Description:

This skill helps agents use a native Swift MCP server to access and automate macOS Apple apps including Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users can use this skill to let an agent inspect and automate local Apple app data on macOS through a Swift MCP server. It supports workflows such as calendar and reminder management, contact lookup and editing, mail and message search or sending, note management, map lookups, and photo organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private Apple app data, including calendars, reminders, contacts, messages, mail, notes, and photos.

Mitigation: Install only when the referenced MCP package is trusted and grant macOS permissions only for data sources needed for the intended workflow.

Risk: The skill can trigger visible or destructive actions such as sending messages or creating, updating, deleting, importing, exporting, or organizing user content.

Mitigation: Require explicit user confirmation before any send, create, update, delete, import, export, or organize action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Project repository](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on local macOS permissions and MCP tool responses from Apple apps.]

## Skill Version(s):

1.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
