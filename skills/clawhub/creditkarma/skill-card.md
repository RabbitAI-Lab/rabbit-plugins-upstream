## Description:

Access Credit Karma transaction data via MCP for syncing transactions, querying spending by category or merchant, reviewing account summaries, and analyzing local financial data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Credit Karma transaction data, sync it into a local SQLite database, and answer personal finance questions about transactions, merchants, categories, and accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses live Credit Karma session cookies and can access sensitive personal financial transaction history.

Mitigation: Install only in a trusted environment and treat CK_COOKIES, copied Cookie headers, .env files, and synced SQLite databases as financial secrets.

Risk: Credentials or transaction data can be exposed through logs, screenshots, shared machines, or repositories.

Mitigation: Avoid capturing or committing secrets and financial data, keep the workspace private, and review logs and screenshots before sharing.

Risk: The fetchproxy path can allow browser-cookie access to the Credit Karma session.

Mitigation: Disable or avoid fetchproxy when browser-cookie access is not desired, and prefer tightly controlled local session handling.

## Reference(s):

- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, SQL]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, MCP tool calls, and SQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include financial transaction summaries and query results derived from a local SQLite database.]

## Skill Version(s):

2.5.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
