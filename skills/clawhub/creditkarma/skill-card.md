## Description:

Access Credit Karma transaction data through an MCP server for syncing, querying, and analyzing spending by category, merchant, account, or custom SQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate a Credit Karma MCP server that syncs transactions locally and answers personal finance questions about transactions, categories, merchants, accounts, and read-only SQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide live Credit Karma session cookies.

Mitigation: Use only on a trusted machine, avoid placing Cookie headers in shared project configuration, and remove stored cookies when no longer needed.

Risk: Syncing creates a local SQLite copy of financial transaction history.

Mitigation: Store the database only in trusted local locations, avoid committing local configuration or data files, and delete local databases when they are no longer needed.

Risk: The security verdict is suspicious because credential and transaction handling have limited safety guidance.

Mitigation: Review the skill carefully before installing and prefer a safer delegated authentication flow if one is available.

## Reference(s):

- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp source repository](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, bash, and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, configuration examples, and read-only SQL examples; results depend on the user's local synced Credit Karma data.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
