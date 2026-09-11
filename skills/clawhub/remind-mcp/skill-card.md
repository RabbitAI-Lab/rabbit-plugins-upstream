## Description:

Read Remind (remind.com) classes, chats, messages, and notification settings from a shell by capturing a signed-in browser session once and querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Remind account, class, chat, message, and notification data from shell workflows without running the Remind MCP server. The skill is read-oriented, but included mutation examples can affect live account state when intentionally executed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill captures reusable Remind session cookies and saves them in a local session file.

Mitigation: Install only when comfortable granting the CLI and browser extension access to the Remind session; protect the saved session file like a password.

Risk: The bundled mutation examples can make live Remind account changes or send messages to real recipients.

Mitigation: Use read queries by default, review variables and recipient identifiers before any mutation, and execute write operations only with explicit intent and valid account permissions.

## Reference(s):

- [Remind GraphQL query examples](references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [Remind web app](https://www.remind.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, curl, GraphQL, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include read queries and clearly marked mutation examples for account changes or message sends.]

## Skill Version(s):

0.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
