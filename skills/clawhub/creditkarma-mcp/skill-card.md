## Description: <br>
Access Credit Karma transaction data via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to connect a local MCP server to Credit Karma, sync transaction data into SQLite, and query spending by account, category, merchant, date, or custom read-only SQL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup can expose live Credit Karma session cookies through CK_COOKIES, copied Cookie headers, .env files, or MCP configuration. <br>
Mitigation: Treat CK_COOKIES and copied Cookie headers like passwords: do not paste them into shared chats, do not commit .env or .mcp.json files, restrict local file access, and revoke or refresh sessions if cookies are exposed. <br>
Risk: The MCP server can access Credit Karma session data and local transaction history. <br>
Mitigation: Install and run it only in an environment where local MCP server access to Credit Karma transactions is acceptable, and review the skill carefully before enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-mcp) <br>
- [npm package](https://www.npmjs.com/package/creditkarma-mcp) <br>
- [Source link from skill artifact](https://github.com/chrischall/creditkarma-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>
- [Credit Karma](https://www.creditkarma.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, code] <br>
**Output Format:** [Markdown with JSON, shell, and SQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces MCP setup guidance and tool-call patterns for syncing and querying local Credit Karma transaction data.] <br>

## Skill Version(s): <br>
2.2.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
