## Description:

Guides agents to read Remind classes, chats, messages, and notification settings using a captured account session and shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Remind account holders and developers use this skill to inspect their classes, conversations, messages, and notification settings from a shell without running the Remind MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A saved login session can grant continued access to a Remind account.

Mitigation: Use only an account you control; protect the session file and delete it when finished.

Risk: Mutation examples can change account settings or send messages to real people.

Mitigation: Avoid mutation examples unless you explicitly intend those changes; check permissions and recipients before sending.

## Reference(s):

- [Remind GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return account data as JSON; examples include jq filters.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
