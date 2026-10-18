## Description:

Helps an agent sync and query a user's Credit Karma transactions, spending, and account balances through a connected service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Credit Karma users can ask an agent to sync their financial data and review transactions, spending by category or merchant, and account balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session cookies give the connected service access to sensitive Credit Karma data.

Mitigation: Use a controlled environment, avoid storing cookies in project configuration that might be committed, and review the external package and browser extension before use.

Risk: Synced financial history remains in local storage after a session is forgotten.

Mitigation: Protect the local transaction database and remove it separately when retention is no longer needed.

## Reference(s):

- [ClawHub creditkarma release](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp package](https://www.npmjs.com/package/creditkarma-mcp)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries and tables of financial data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on successful synchronization; credit-report balances may lag live account balances.]

## Skill Version(s):

3.3.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
