## Description:

Guides agents in accessing and managing Splitwise expenses, groups, friends, balances, and receipts through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers using an agent can check shared expenses and balances, manage Splitwise groups and expenses, and retrieve receipts after configuring the Splitwise MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating, editing, or deleting Splitwise records can change shared financial data.

Mitigation: Review the proposed change and confirmation preview before approving a write.

Risk: The Splitwise API key and returned financial data are sensitive.

Mitigation: Keep the API key private and limit access to balances, expenses, and receipts.

Risk: Downloaded receipts may be written to the server's working directory.

Mitigation: Use a constrained receipt output directory or request inline receipt content when local files are unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise API key registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Shell commands]

**Output Format:** [Markdown with JSON configuration and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains Splitwise read and write workflows, including confirmation previews and receipt handling.]

## Skill Version(s):

3.2.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
