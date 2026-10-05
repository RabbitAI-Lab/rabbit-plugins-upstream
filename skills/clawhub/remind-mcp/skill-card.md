## Description:

Guides agents in reading Remind classes, chats, messages, and notification settings from a signed-in account using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with a Remind account use this skill to retrieve their classes, conversations, messages, and notification settings without running the Remind MCP server. Developers can also adapt the supplied shell queries for scripts or one-off checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured, reusable Remind session credential is stored locally.

Mitigation: Review the credential capture before installing, protect the saved session file, and delete or rotate the session when it is no longer needed.

Risk: The reference examples include mutations that change notification settings or send messages to real people.

Mitigation: Use read-only queries by default; run mutations only when you intentionally want to change settings or send a message.

## Reference(s):

- [Remind-mcp ClawHub release](https://clawhub.ai/chrischall/skills/remind-mcp)
- [Remind GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results may include account details and message content.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
