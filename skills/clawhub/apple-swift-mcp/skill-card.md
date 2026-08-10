## Description:

This skill enables agents to use a native Swift MCP server to inspect and automate Apple app data across Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent access and automate local Apple app workflows on macOS, including scheduling, reminders, contacts, maps, email, messages, notes, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose private macOS app data, including mail, messages, notes, contacts, calendars, reminders, and photos.

Mitigation: Install only trusted releases, grant the minimum macOS permissions needed, and review data access requests before allowing the agent to proceed.

Risk: The skill supports write actions such as sending communications, deleting or updating records, exporting photos, and modifying app data.

Mitigation: Require explicit user approval before sending messages or mail, deleting or updating records, exporting photos, or making other persistent changes.

Risk: Messages history access can read chat.db and may reveal sensitive conversation history.

Mitigation: Avoid granting full disk access unless Messages history is required, and restrict use to narrowly scoped requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [Project Repository](https://github.com/chrischall/apple-swift-mcp)
- [GitHub Releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires macOS 14+ on Apple Silicon; access depends on granted macOS permissions.]

## Skill Version(s):

1.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
