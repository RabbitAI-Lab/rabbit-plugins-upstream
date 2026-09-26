## Description:

Helps agents access and manage Calendar, Reminders, Contacts, Maps, Mail, Messages, Notes, and Photos on macOS through a native Swift MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and macOS users can use this skill to help an agent find personal app data, manage calendars and reminders, and perform approved actions such as sending messages or updating contacts and photos. The packaged server requires macOS 14 or later on Apple Silicon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to Mail, Messages, Notes, Contacts, and Photos may expose sensitive personal data.

Mitigation: Grant only necessary permissions and favor read-only tool access; treat Full Disk Access and photo export or import with particular care.

Risk: Installation relies on a downloadable binary whose version is not pinned in the skill instructions.

Mitigation: Review the GitHub release and requested permissions before installing.

Risk: Confirmation does not cover every write or export action, and automatic confirmation can send or delete without a user prompt.

Mitigation: Review write and export requests before execution, and avoid MCP_CONFIRM_MODE=auto unless automatic sends and deletes are explicitly acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [GitHub project linked in skill documentation](https://github.com/chrischall/apple-swift-mcp)
- [GitHub releases linked in skill documentation](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Structured tool results]

**Output Format:** [Markdown guidance and structured MCP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include sensitive personal data; write tools may send messages or change app data.]

## Skill Version(s):

2.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
