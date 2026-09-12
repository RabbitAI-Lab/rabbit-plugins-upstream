## Description:

Accesses Credit Karma transaction data through an MCP server so agents can sync transactions, summarize accounts, and answer spending questions by category or merchant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their Credit Karma transaction data, sync it to a local SQLite database, and query spending, merchant, category, account, and read-only SQL summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to expose or persist sensitive Credit Karma session cookies.

Mitigation: Use only on trusted machines, avoid project-local environment files for cookies, restrict file permissions, and prefer a secret manager or safer official authentication flow when available.

Risk: The MCP stores sensitive financial transaction data in a local SQLite database.

Mitigation: Treat the database as sensitive financial data, limit local access, and review storage location and retention before use.

Risk: The skill installs and runs a third-party MCP package.

Mitigation: Pin and verify the MCP package or source before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, SQL]

**Output Format:** [Markdown with JSON, bash, and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs help configure and use an MCP server that stores synced financial transactions in a local SQLite database.]

## Skill Version(s):

2.8.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
