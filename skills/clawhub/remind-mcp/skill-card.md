## Description:

Helps agents read Remind classes, chats, messages, and notification settings from a shell using a captured signed-in session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Remind users and developers use this skill to inspect their account's classes, conversations, messages, and notification settings through shell commands without running the Remind MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured session credentials can grant access to the signed-in Remind account if disclosed.

Mitigation: Keep the session file private, out of backups and shared directories, and delete it when finished.

Risk: The included mutation examples can change notification settings or send messages to real people despite the skill's read-oriented purpose.

Mitigation: Do not run mutation examples unless you explicitly intend the change; review recipients and permissions before sending messages.

## Reference(s):

- [Remind GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [remind-mcp ClawHub release](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Remind session for live queries.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
