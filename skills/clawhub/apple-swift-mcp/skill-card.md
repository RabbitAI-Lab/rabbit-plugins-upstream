## Description: <br>
This skill helps an agent work with local Apple app data through a native Swift MCP server for Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos on macOS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and macOS users use this skill to let an agent search, read, create, update, send, organize, import, export, or delete data in local Apple apps. It is intended for macOS 14+ on Apple Silicon, with some operations requiring Apple TCC permissions or app automation access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive local Apple app data including calendar entries, contacts, emails, messages, notes, photos, and reminders. <br>
Mitigation: Grant only the app and disk permissions needed for the current task, and review requested data access before allowing the agent to proceed. <br>
Risk: The skill supports write or state-changing actions such as sending messages or mail, creating or deleting events and reminders, exporting photos, and changing photo metadata. <br>
Mitigation: Require explicit user confirmation before send, delete, update, export, import, or metadata-changing actions. <br>
Risk: Messages history may require direct local database access, and AppleScript-backed app automation can operate on personal application data. <br>
Mitigation: Avoid broad full-disk or automation permissions unless the user understands which local data stores will be readable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp) <br>
- [apple-swift-mcp GitHub repository](https://github.com/chrischall/apple-swift-mcp) <br>
- [apple-swift-mcp GitHub releases](https://github.com/chrischall/apple-swift-mcp/releases) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with tool-use guidance, commands, and configuration notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on macOS 14+, Apple Silicon, local app permissions, and user confirmation for sensitive read or write actions.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
