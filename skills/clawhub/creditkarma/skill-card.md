## Description:

Access Credit Karma transaction data through an MCP server for syncing, filtering, and analyzing personal finance transactions, spending categories, merchants, and account summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Credit Karma MCP server that syncs financial transaction data into a local SQLite database and supports spending analysis, account summaries, and read-only SQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires local tooling or a browser extension to access active Credit Karma session cookies and locally stored financial transaction data.

Mitigation: Install only after reviewing the third-party MCP server and extension, prefer a pinned reviewed version, and grant access only in environments where exposure of financial session data is acceptable.

Risk: Credential material such as Credit Karma cookies may be stored in environment variables, MCP configuration, or a local .env file.

Mitigation: Keep .env and MCP configuration files out of source control and backups, avoid storing cookies in project files, rotate or remove stored credentials when no longer needed, and delete the local database after use.

## Reference(s):

- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp source repository](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, code, text]

**Output Format:** [Markdown with JSON, bash, SQL, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to configure MCP access, sync local transaction data, and return transaction summaries or read-only query results.]

## Skill Version(s):

2.8.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
