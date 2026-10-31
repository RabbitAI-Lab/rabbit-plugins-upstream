## Description:

Access Credit Karma transaction data through MCP tools for transaction, spending, account-summary, and balance queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Credit Karma users can sync and review their financial transactions, spending patterns, account summaries, and balances. The skill supports developers configuring the MCP connection and users querying their own data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One setup path passes reusable Credit Karma login cookies through chat or assistant-visible tool arguments.

Mitigation: Use a local authentication route instead; review and pin the server and extension, and approve only necessary Credit Karma access.

Risk: The local database contains financial data, and forgetting a session does not delete the database or revoke the account session.

Mitigation: Protect the local financial database; do not treat forgetting a session as deleting stored data or revoking the Credit Karma session.

## Reference(s):

- [Credit Karma MCP package](https://www.npmjs.com/package/creditkarma-mcp)
- [Credit Karma](https://www.creditkarma.com)

## Skill Output:

**Output Type(s):** [Analysis, Text, Transaction and account data]

**Output Format:** [Natural-language summaries and structured query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect the available synced financial data.]

## Skill Version(s):

3.3.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
