## Description:

Access Credit Karma transaction data through the creditkarma-mcp MCP server for syncing, querying, and analyzing local transaction records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Credit Karma transaction data, sync transactions into a local SQLite database, and answer spending, merchant, category, account summary, and read-only SQL questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on live Credit Karma session cookies and may store them in local configuration files.

Mitigation: Protect .env and MCP configuration files, exclude them from source control, and refresh or revoke the Credit Karma session after use.

Risk: The recommended npx setup can execute an unpinned creditkarma-mcp package.

Mitigation: Audit and pin the exact package or source version before installing or running the MCP server.

Risk: Synced transaction data is stored locally and can include sensitive financial history.

Mitigation: Limit local database access to trusted users and remove local synced data when it is no longer needed.

## Reference(s):

- [creditkarma ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp source repository](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy extension source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and SQL examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include MCP setup steps and queries that operate on locally synced Credit Karma transaction data.]

## Skill Version(s):

2.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
