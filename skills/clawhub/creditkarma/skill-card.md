## Description: <br>
Access Credit Karma transaction data via MCP for syncing transactions, reviewing account summaries, and analyzing spending by category, merchant, date range, or read-only SQL queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to their Credit Karma transaction data, sync it into a local SQLite database, and answer personal finance questions about spending, merchants, accounts, and categories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live Credit Karma session cookies and local transaction history. <br>
Mitigation: Install only if comfortable granting MCP access to the active Credit Karma session and protect CK_COOKIES, local configuration, .env files, and generated databases as password-equivalent sensitive data. <br>
Risk: The setup can read browser cookies through the fetchproxy extension or persist copied cookies through ck_set_session. <br>
Mitigation: Review the fetched npm package and browser extension before use, avoid pasting cookies into chat when possible, and delete stored credentials and local data when no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma) <br>
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>
- [Credit Karma](https://www.creditkarma.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline JSON, bash, SQL, and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides MCP setup and produces agent-facing instructions for authentication, transaction syncing, filtered queries, spending summaries, account summaries, and read-only SQL analysis.] <br>

## Skill Version(s): <br>
2.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
