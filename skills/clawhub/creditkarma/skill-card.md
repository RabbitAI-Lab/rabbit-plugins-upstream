## Description:

Helps agents sync and analyze a user's Credit Karma transactions, spending, and account summaries through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with Credit Karma accounts use this skill to sync their transactions and ask an agent for spending breakdowns, merchant totals, and account summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live Credit Karma session cookies grant access to a financial account and may be exposed through configuration, the saved session, or the optional browser extension.

Mitigation: Install only if comfortable with this access; treat cookies and the saved session as account credentials, limit access, and use the forget-session tool when finished.

Risk: Synced transaction history remains in a local database, even after the saved session is forgotten.

Mitigation: Protect the local database and remove it separately when the transaction history is no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp package and setup](https://www.npmjs.com/package/creditkarma-mcp)
- [Optional fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Analysis, SQL queries]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain sensitive financial transaction data.]

## Skill Version(s):

3.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
