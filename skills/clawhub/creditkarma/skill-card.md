## Description:

Access Credit Karma transaction data through an MCP server for syncing transactions, querying spending by category or merchant, viewing account summaries, and performing local SQL analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure creditkarma-mcp, sync their Credit Karma transactions into a local SQLite database, and ask agents to analyze personal spending, merchants, categories, and account summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Credit Karma session cookies that can function as sensitive financial credentials.

Mitigation: Treat CK_COOKIES and copied Cookie headers as secrets; do not commit, log, or share them, and rotate or refresh them if exposed.

Risk: The skill stores a local SQLite copy of transaction history containing sensitive financial records.

Mitigation: Store the database only in trusted local locations, restrict file access, and avoid sharing project directories that contain the database or .env file.

Risk: The optional fetchproxy path can read browser session cookies automatically.

Mitigation: Use the manual CK_COOKIES path or disable the fetchproxy fallback if automatic browser-cookie access is not acceptable.

## Reference(s):

- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, SQL queries, MCP tool calls, Guidance]

**Output Format:** [Markdown with JSON, bash, and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local transaction summaries, spending analyses, account summaries, MCP setup snippets, and read-only SQL queries.]

## Skill Version(s):

2.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
