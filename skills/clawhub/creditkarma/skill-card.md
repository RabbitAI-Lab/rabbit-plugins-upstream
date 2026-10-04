## Description:

Helps agents sync and query a user's Credit Karma transactions, spending, and account summaries through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use this skill to sync Credit Karma transactions locally and review spending by category, merchant, or account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit Karma session cookies grant access to sensitive financial data and may be exposed in chat, configuration, logs, or screenshots.

Mitigation: Keep cookies out of chats, logs, and screenshots; protect stored credentials and use ck_forget_session when finished.

Risk: Third-party MCP and browser-extension code can read session cookies, and synced transactions remain in a local database.

Mitigation: Review the npm package or source and the ContextMint Bridge extension before use; protect and manage the local transaction database separately from saved sessions.

## Reference(s):

- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, SQL queries, Configuration instructions]

**Output Format:** [Markdown guidance and transaction summaries; structured MCP query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require a local transaction sync; SQL reads are limited to 5,000 rows.]

## Skill Version(s):

3.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
