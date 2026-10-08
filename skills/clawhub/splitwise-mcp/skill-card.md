## Description:

Helps agents use Splitwise to check balances, groups, friends, and expenses and manage shared-expense records through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents managing shared expenses use this skill to review Splitwise balances and records, add or edit expenses, manage groups and friends, and retrieve receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installed package receives a Splitwise API key and can read account balances, friends, expenses, and receipts.

Mitigation: Confirm that you trust the package before providing it with your Splitwise API key.

Risk: Approved write actions can create, change, delete, or restore Splitwise records.

Mitigation: Review the proposed changes and approve writes only when they match your intent.

Risk: Receipt retrieval can save files to the server filesystem.

Mitigation: Use inline receipt or text extraction modes when you do not want receipt files saved on the server.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, MCP tool calls]

**Output Format:** [Markdown with JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results can include Splitwise account data and receipts.]

## Skill Version(s):

3.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
