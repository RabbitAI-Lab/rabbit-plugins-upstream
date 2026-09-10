## Description:

Access Credit Karma transaction data via MCP. Use when the user asks about their Credit Karma transactions, spending by category or merchant, account summaries, or wants to sync or query their financial data. Triggers on phrases like "sync my transactions", "what did I spend on", "show my Credit Karma data", "spending by category", "top merchants", or any request involving personal finance data from Credit Karma. Requires creditkarma-mcp installed and the creditkarma server registered (see Setup below).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate a Credit Karma MCP server for syncing transaction data, reviewing account summaries, and querying personal spending by date, merchant, category, account, or read-only SQL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can expose and persist sensitive Credit Karma session cookies and local transaction history.

Mitigation: Install only if that access is acceptable; avoid pasted Cookie headers and plaintext .env/config storage when possible, keep credential files out of source control, restrict file access, and remove credentials when finished.

Risk: The workflow relies on unpinned external MCP and browser-extension code.

Mitigation: Review the creditkarma-mcp package and fetchproxy extension source and version before installation or use.

## Reference(s):

- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp source repository](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Code]

**Output Format:** [Markdown with JSON, bash, and SQL code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP setup guidance, tool usage examples, and read-only SQL query examples.]

## Skill Version(s):

2.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
