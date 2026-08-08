## Description:

Access Credit Karma transaction data through an MCP server for transaction sync, account summaries, spending analysis, and filtered financial queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to configure creditkarma-mcp, sync Credit Karma transactions into local SQLite, and answer personal finance questions by category, merchant, account, or SQL query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to expose and persist Credit Karma session cookies for access to sensitive financial data.

Mitigation: Treat CK_COOKIES and copied Cookie headers like passwords; do not paste them into chats, logs, screenshots, or repositories, and delete any .env file and local SQLite database when no longer needed.

Risk: A local MCP server and optional browser extension can access the user's Credit Karma session and transaction history.

Mitigation: Install only when comfortable granting that local access, and review the MCP server and extension before use.

## Reference(s):

- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp source](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, bash, and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP setup guidance and tool usage examples.]

## Skill Version(s):

2.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
