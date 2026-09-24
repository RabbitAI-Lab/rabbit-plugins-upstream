## Description:

remind-mcp helps agents read Remind classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Remind account, class, chat, message, and notification data through documented shell commands, mainly for one-shot queries or scripts without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents live write-capable GraphQL mutations while presenting itself as read-oriented.

Mitigation: Review before installing if read-only Remind access is required, and avoid mutation examples unless deliberately changing account settings or sending messages.

Risk: Captured Remind session headers can grant account access if exposed.

Mitigation: Treat the saved session file like a password, restrict file permissions, remove it when finished, and avoid storing it in shared locations.

Risk: Message-sending mutations can contact real recipients and cannot be unsent.

Mitigation: Check permissions such as canSend first and use write examples only with explicit intent and an account authorized for that action.

## Reference(s):

- [Remind GraphQL ready-to-run documents](references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [Remind web app](https://www.remind.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and GraphQL/curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes jq recipes and cautions for session handling, authorization failures, introspection, and write-capable mutations.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
