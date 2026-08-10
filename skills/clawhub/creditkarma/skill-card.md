## Description:

Accesses Credit Karma transaction data via MCP for syncing, summarizing, and querying personal finance records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate creditkarma-mcp for syncing Credit Karma transactions into a local SQLite database and querying spending, merchants, categories, accounts, or custom read-only SQL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires sensitive Credit Karma session cookies and may store local financial transaction history.

Mitigation: Treat CK_COOKIES, copied Cookie headers, .env files, and the SQLite database as sensitive financial secrets; use a dedicated project and avoid sharing cookies in chat.

Risk: The security scan verdict is suspicious because the unofficial MCP server and browser extension can access a Credit Karma session and local transaction data.

Mitigation: Inspect the package and extension before use, install only if that access is acceptable, and revoke or refresh sessions after any exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, shell, and SQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides MCP setup and use for transaction syncing, summaries, filtered queries, and read-only SQL analysis.]

## Skill Version(s):

2.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
