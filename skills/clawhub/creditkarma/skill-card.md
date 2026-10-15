## Description:

Helps agents sync and analyze a user's Credit Karma transactions, spending, and account balances through a connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with access to their Credit Karma account can sync transactions and ask for spending breakdowns, transaction history, account summaries, and balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP package and optional browser bridge handle live Credit Karma session cookies and sensitive financial information.

Mitigation: Review and pin the package and bridge before installation; consider a dedicated browser profile and avoid sharing Cookie headers in chat or configuration unless necessary.

Risk: Copies of financial transactions and saved session credentials remain on the local device.

Mitigation: Restrict access to local data and delete both the saved session and transaction database when no longer needed.

## Reference(s):

- [creditkarma-mcp package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp source](https://github.com/chrischall/creditkarma-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with transaction and spending summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial figures may reflect the last sync; credit-report balances can lag linked-account balances.]

## Skill Version(s):

3.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
