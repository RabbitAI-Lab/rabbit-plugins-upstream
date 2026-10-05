## Description:

Helps an agent sync and analyze a user's Credit Karma transactions, including spending by category, merchant, and account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Credit Karma users and their agents use this skill to sync transactions and answer questions about spending, merchants, and account activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser cookies and saved sessions grant access to a live Credit Karma account.

Mitigation: Use a dedicated environment, handle Cookie headers as credentials, and review the MCP package and browser extension before granting access.

Risk: Transaction history containing sensitive financial data is stored locally and remains after the session is forgotten.

Mitigation: Confirm how to remove both saved sessions and the local transaction database, and protect the device storing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/creditkarma)
- [creditkarma-mcp package](https://www.npmjs.com/package/creditkarma-mcp)
- [creditkarma-mcp source linked by the skill](https://github.com/chrischall/creditkarma-mcp)
- [ContextMint Bridge source linked by the skill](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Markdown or plain text with transaction summaries and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial answers depend on locally synced transaction data.]

## Skill Version(s):

3.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
