## Description:

This skill helps an agent work with Apple app data through a native Swift MCP server for Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and macOS users use this skill to let an agent inspect and manage local Apple app data, including calendar items, reminders, contacts, maps, mail, messages, notes, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive local Apple app data such as contacts, calendar entries, photos, mail, messages, notes, and chat history.

Mitigation: Install only if the publisher is trusted, grant only required macOS permissions, and review requested TCC access before use.

Risk: The skill can perform outbound or state-changing operations such as sending messages or mail, updating records, deleting items, exporting photos, or importing data.

Mitigation: Use explicit prompts and require human confirmation before send, delete, export, import, create, or update actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [GitHub repository](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with optional shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve local macOS app permissions and user confirmation for sensitive actions.]

## Skill Version(s):

1.4.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
