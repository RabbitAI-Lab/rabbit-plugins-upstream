## Description:

Access Credit Karma transaction data via MCP for transaction syncing, spending analysis, account summaries, and natural-language queries over local financial data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure a Credit Karma MCP server, sync transactions to a local SQLite database, and query spending by category, merchant, account, date range, or read-only SQL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to Credit Karma session cookies, which can expose live financial-session credentials if copied, stored, or shared unsafely.

Mitigation: Treat CK_COOKIES and copied Cookie headers like passwords, avoid plaintext storage where possible, and refresh or revoke sessions if exposure is suspected.

Risk: The configured MCP can access transaction history and sync personal financial data into a local SQLite database.

Mitigation: Use explicit user confirmation before syncing or querying financial data, restrict local database access, and install only after reviewing the external package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, code]

**Output Format:** [Markdown with JSON, shell, and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides MCP setup and tool usage; the configured MCP can sync and query local SQLite transaction data.]

## Skill Version(s):

3.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
