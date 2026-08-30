## Description:

Access Credit Karma transaction data via MCP for syncing transactions, reviewing spending by category or merchant, viewing account summaries, and querying local financial data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate a Credit Karma MCP server for syncing personal transaction data into local SQLite storage and querying spending, merchants, categories, accounts, and read-only SQL views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses live Credit Karma session cookies and optional browser-cookie access.

Mitigation: Treat CK_COOKIES and copied Cookie headers like passwords, avoid shared machines, and prefer setups where secrets can be controlled or revoked.

Risk: The skill stores personal financial transaction data locally.

Mitigation: Use the skill only on trusted machines and review local data handling before syncing transactions.

Risk: The server security verdict is suspicious because credential scope and warnings are limited.

Mitigation: Review the third-party package and optional browser extension before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [Credit Karma](https://www.creditkarma.com)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON, bash, SQL, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents through MCP setup, transaction sync, local SQLite querying, and read-only financial analysis workflows.]

## Skill Version(s):

2.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
