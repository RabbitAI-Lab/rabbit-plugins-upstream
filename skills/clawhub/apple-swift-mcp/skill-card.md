## Description:

Provides agent access to Apple app data and actions through a native Swift MCP server for Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and macOS users use this skill to let an agent search, read, create, update, delete, send, organize, import, or export information across supported Apple apps through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Apple app data and perform high-impact write actions such as sending messages or email and changing contacts, events, notes, reminders, or photos.

Mitigation: Install only from a trusted project and require explicit user confirmation before any send, delete, update, import, or export action.

Risk: Some reads may require broad macOS permissions, including Full Disk Access for data sources such as Mail indexes or Messages history.

Mitigation: Grant only the permissions needed for the intended workflow and treat read-only queries as lower risk than actions that modify or transmit data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [apple-swift-mcp GitHub project](https://github.com/chrischall/apple-swift-mcp)
- [apple-swift-mcp GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with tool usage guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of tools that read or change local Apple app data after macOS permission prompts.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
