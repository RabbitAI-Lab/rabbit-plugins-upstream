## Description:

Guides agents in reading Remind classes, chats, messages, and notification settings through shell-based GraphQL queries using a captured signed-in session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Remind users can ask an agent to retrieve account, class, conversation, message, and notification information without running the Remind MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The captured Remind session can be reused to access the account.

Mitigation: Treat the session file like a password, restrict its access, and delete it when finished.

Risk: Bundled GraphQL mutations can change settings or send messages to real people.

Mitigation: Supervise GraphQL calls and avoid mutation examples unless a specific change or message is explicitly intended.

## Reference(s):

- [Remind GraphQL query examples](references/graphql-queries.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/remind-mcp)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented queries; the references also include write-capable mutation examples.]

## Skill Version(s):

1.2.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
