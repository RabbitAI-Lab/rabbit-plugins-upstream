## Description:

Helps agents read and manage Splitwise expenses, groups, friends, and balances through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Splitwise can ask an agent to review balances and shared expenses, manage groups and friends, and make approved changes to expense records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive Splitwise financial data and account credentials.

Mitigation: Install only for intended account access, review the package, and safeguard the Splitwise API key.

Risk: Expense, group, friend, comment, or user changes may alter shared records.

Mitigation: Review the proposed changes with the user and obtain confirmation before approving writes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise API key registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Shell commands]

**Output Format:** [Markdown with optional JSON configuration and Splitwise tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include expense details, balances, group information, and receipts on request.]

## Skill Version(s):

3.2.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
