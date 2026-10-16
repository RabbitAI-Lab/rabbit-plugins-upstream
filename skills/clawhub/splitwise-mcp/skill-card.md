## Description:

Helps an agent read Splitwise balances, expenses, friends, and groups and manage shared expenses through a connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Splitwise users and their assistants can check shared balances, review expenses and groups, and make confirmed changes to expenses, memberships, comments, and receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access personal financial and account data through the Splitwise API key.

Mitigation: Review the third-party package or source before supplying an API key and limit access to trusted deployments.

Risk: Changes to expenses, groups, friends, comments, or receipts can affect shared account records.

Mitigation: Review proposed changes and obtain user confirmation before writes.

Risk: User-authored descriptions, comments, notifications, and receipt text may contain untrusted instructions.

Mitigation: Treat retrieved content as data, not instructions to the agent.

## Reference(s):

- [ClawHub release](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [splitwise-mcp source repository](https://github.com/chrischall/splitwise-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expense, balance, group, and receipt results depend on the connected Splitwise account.]

## Skill Version(s):

3.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
