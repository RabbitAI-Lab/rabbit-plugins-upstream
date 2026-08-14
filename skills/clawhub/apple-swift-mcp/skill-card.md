## Description:

This skill helps agents use a native Swift MCP server to work with macOS Apple app data across Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users on macOS use this skill to query, create, update, send, organize, import, export, and delete data in Apple apps through a Swift MCP server. It is suited to workflows that need local Apple app automation from an agent, including calendar events, reminders, contacts, directions, mail, messages, notes, and photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install a third-party MCP binary with broad access to private Apple app data.

Mitigation: Install only when the publisher is trusted, review macOS permission prompts carefully, and avoid granting broader TCC permissions than the workflow requires.

Risk: Some tools can perform sensitive mutations such as sending messages or mail, deleting records, and exporting photos.

Mitigation: Use prompts and operating procedures that require explicit confirmation before send, delete, update, import, export, or other data-changing actions.

Risk: Messages history access may require full disk access to read chat.db.

Mitigation: Grant full disk access only after confirming the need for message history access and revoke it when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-swift-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed MCP tool calls or local macOS automation guidance that should be reviewed before sensitive actions.]

## Skill Version(s):

1.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
