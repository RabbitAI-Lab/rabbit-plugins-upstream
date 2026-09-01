## Description:

Access Credit Karma transaction data via MCP. Use when the user asks about their Credit Karma transactions, spending by category or merchant, account summaries, or wants to sync or query their financial data. Triggers on phrases like "sync my transactions", "what did I spend on", "show my Credit Karma data", "spending by category", "top merchants", or any request involving personal finance data from Credit Karma. Requires creditkarma-mcp installed and the creditkarma server registered (see Setup below).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and query a Credit Karma MCP server for transaction sync, spending analysis, merchant/category summaries, account summaries, and read-only SQL over locally synced financial data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to Credit Karma session cookies and can sync sensitive financial transactions to a local SQLite database.

Mitigation: Install only if this access is acceptable, treat CK_COOKIES, CKAT, CKTRKID, copied Cookie headers, and the local database like secrets, and remove local credentials or refresh Credit Karma sessions if exposed.

Risk: The fetchproxy path can read browser cookies for Credit Karma on first tool use.

Mitigation: Disable or avoid fetchproxy when browser-cookie access is not desired, and prefer explicit session handling with carefully protected credentials.

Risk: The release security verdict is suspicious because user-facing controls and warnings are limited for highly sensitive financial access.

Mitigation: Review the package before deployment, pin and verify the npm package, and confirm local storage and credential handling meet the user's security expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp repository linked by skill](https://github.com/chrischall/creditkarma-mcp)
- [fetchproxy extension repository linked by skill](https://github.com/chrischall/fetchproxy)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, bash, SQL, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides MCP setup and use; queried financial data is produced by the configured MCP server.]

## Skill Version(s):

2.7.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
