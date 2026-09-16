## Description:

Access Credit Karma transaction data via MCP for syncing, querying, and analyzing personal financial transaction data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a local Credit Karma MCP server, sync transaction data, and answer spending, merchant, category, account summary, and read-only SQL questions over the local SQLite copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a live Credit Karma session and transaction history through cookies, a browser extension, or locally stored credentials.

Mitigation: Install only after reviewing the third-party MCP server and extension, pin the package or source to an audited version, keep credential files out of version control and backups, and remove stored cookies and the local SQLite database before using shared or less-trusted machines.

Risk: Synced personal finance data is stored locally in SQLite.

Mitigation: Treat the database as sensitive financial data, restrict local file access, avoid sharing the workspace, and delete the database when it is no longer needed.

## Reference(s):

- [Credit Karma MCP npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [Credit Karma MCP source](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Text]

**Output Format:** [Markdown with JSON, bash, SQL, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agent use of an MCP server that syncs Credit Karma data into local SQLite and exposes read-only query tools.]

## Skill Version(s):

2.8.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
