## Description:

Helps an agent sync and query a user's Credit Karma transactions, spending, accounts, and balances through a separately installed MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Credit Karma users can ask an agent to sync their financial data and summarize transactions, spending by category or merchant, and account balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable financial session cookies may be exposed through chat, configuration files, or an optional browser bridge.

Mitigation: Review the third-party server and bridge before connecting; use the narrowest local setup and avoid pasting Cookie headers into ordinary chat or shared logs.

Risk: Synced transactions and balances persist locally even after the saved session is forgotten.

Mitigation: Understand where the session and local financial database are stored, and delete both when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp project](https://github.com/chrischall/creditkarma-mcp)
- [Optional ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown summaries and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries depend on synced data; credit-report balances may lag.]

## Skill Version(s):

3.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
