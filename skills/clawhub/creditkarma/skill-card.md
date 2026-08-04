## Description: <br>
Access Credit Karma transaction data via MCP for transaction sync, spending analysis, account summaries, and natural-language queries against local financial data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure a Credit Karma MCP server, sync personal transaction data into a local SQLite database, and query spending by transaction, category, merchant, account, or read-only SQL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Credit Karma session cookies, including CK_COOKIES or copied Cookie headers, to authenticate MCP access. <br>
Mitigation: Treat cookies as passwords, keep them out of shared logs and synced folders, and rotate or delete them when access is no longer needed. <br>
Risk: The optional browser extension path can access active Credit Karma session cookies from the signed-in browser. <br>
Mitigation: Use the extension only in a trusted browser profile, sign out or remove the extension after setup when appropriate, and avoid using it on shared machines. <br>
Risk: Synced Credit Karma transactions are stored locally in SQLite and may contain sensitive financial history. <br>
Mitigation: Store the database only in a protected local workspace, avoid shared or cloud-synced project folders, and delete the database when it is no longer needed. <br>


## Reference(s): <br>
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp) <br>
- [creditkarma-mcp GitHub project](https://github.com/chrischall/creditkarma-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>
- [Credit Karma](https://www.creditkarma.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown with JSON, shell, and SQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agent use of MCP tools that can sync and query local SQLite transaction data.] <br>

## Skill Version(s): <br>
2.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
