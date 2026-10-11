## Description:

Helps an agent sync and analyze Credit Karma transactions, spending, accounts, and balances through the creditkarma-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Credit Karma users can ask an agent to sync their transactions and summarize spending by category, merchant, or account, or check account balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication grants the server access equivalent to a logged-in Credit Karma session.

Mitigation: Review the npm package, source repository, and browser extension before installing; do not paste cookies into shared configuration files.

Risk: Synced transactions and balances remain on local disk after saved session credentials are removed.

Mitigation: Protect local financial data and manage the transaction database separately; forgetting the session does not delete it.

## Reference(s):

- [Creditkarma skill release](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp npm package](https://www.npmjs.com/package/creditkarma-mcp)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language financial summaries and transaction lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on synced Credit Karma data; credit-report balances can lag live balances.]

## Skill Version(s):

3.3.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
