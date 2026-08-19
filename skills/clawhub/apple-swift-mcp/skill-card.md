## Description:

This skill lets an agent access and automate Apple app data on macOS through a native Swift MCP server for Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

macOS users and developers use this skill to let an agent search, read, create, update, send, delete, and organize data across native Apple apps. It is intended for local Apple app automation workflows on macOS 14+ with Apple Silicon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad personal data across Apple apps, including Mail, Messages, Notes, Photos, Calendar, Contacts, and related app data.

Mitigation: Install only when that access is needed, review macOS permission prompts carefully, and grant the minimum permissions required for the intended workflow.

Risk: Full Disk Access may expose direct Mail or Messages history search data.

Mitigation: Avoid granting Full Disk Access unless direct Mail or Messages history search is required.

Risk: The skill can send messages, delete items, export photos, or change notes and events.

Mitigation: Require explicit confirmation before any send, delete, export, or data-changing action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Artifact-listed GitHub project](https://github.com/chrischall/apple-swift-mcp)
- [Artifact-listed GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with MCP tool-use guidance and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in macOS app actions and file exports when the agent invokes the MCP tools.]

## Skill Version(s):

1.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
