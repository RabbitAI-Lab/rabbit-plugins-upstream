## Description:

Guides agents in reading Remind classes, chats, messages, and notification settings from a shell using a captured browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Remind users and developers use this skill to inspect their classes, chats, messages, and notification settings through shell-based queries without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing a full signed-in Remind browser session gives shell access to account data and actions.

Mitigation: Keep the session file private, restrict access to it, and delete or rotate it when finished.

Risk: The included mutation examples can change settings or send real messages despite the read-oriented description.

Mitigation: Review commands before execution and allow mutations only when you explicitly intend the changes or messages.

## Reference(s):

- [Remind GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return data available to the signed-in Remind account.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
