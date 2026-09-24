## Description:

Provides agent access to Apple app data on macOS through the native Swift MCP for Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users and agents use this skill to read, search, create, update, and delete supported Apple app data through a native Swift MCP server. It is intended for workflows involving personal productivity data such as calendars, reminders, contacts, mail, messages, notes, photos, maps, and related macOS app automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify private Apple app data, including mail, messages, contacts, calendars, notes, and photos.

Mitigation: Install only from a trusted source, grant the minimum macOS permissions needed for the task, and review read and write requests before approving them.

Risk: Some actions can send messages, send mail, delete records, or update contacts and recurring calendar events.

Mitigation: Use explicit prompts for write operations and confirm recipients, targets, recurrence spans, and deletion scope before executing changes.

Risk: Full Disk Access may expose sensitive local stores such as Mail indexes or Messages history.

Mitigation: Avoid granting Full Disk Access unless history or indexed message search is actually required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Project repository](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and natural-language tool guidance with inline commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide MCP tool calls that read or modify local Apple app data after macOS permission prompts are granted.]

## Skill Version(s):

1.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
