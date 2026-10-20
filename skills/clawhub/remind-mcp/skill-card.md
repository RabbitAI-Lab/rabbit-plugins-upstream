## Description:

Helps an agent read Remind classes, chats, messages, and notification settings through shell-based GraphQL queries using a captured browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Remind users can inspect their classes, chats, messages, and notification settings from a shell or one-off script without running the Remind MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable Remind login session is stored on disk and could expose account data if disclosed.

Mitigation: Keep the session file private; delete or rotate the session when finished.

Risk: The query reference includes write-capable examples that could change notification settings or send real messages despite the read-oriented framing.

Mitigation: Enforce read-only use unless changes are explicitly intended; review mutations before execution.

## Reference(s):

- [Remind GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [remind-mcp on ClawHub](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples return Remind account data, often as JSON or readable text.]

## Skill Version(s):

1.2.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
