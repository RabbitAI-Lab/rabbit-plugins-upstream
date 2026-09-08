## Description:

splitwise-mcp lets agents access Splitwise expense, group, friend, balance, receipt, and notification data through an MCP server and perform supported Splitwise account changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent answer questions about Splitwise balances, groups, friends, expenses, notifications, and receipts, and to help create or update shared-expense records when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify live Splitwise data, including expense edits, deletes, restores, and group or friend changes.

Mitigation: Review write actions before execution, especially record IDs, amounts, split details, and delete operations.

Risk: The configured Splitwise API key grants account access to any agent or MCP server process that can use it.

Mitigation: Store the API key only in trusted local configuration, avoid sharing configs or logs that contain it, and remove access when the skill is no longer needed.

Risk: Receipt handling may expose personal financial documents or write files to an MCP server filesystem the user cannot directly inspect.

Mitigation: Prefer inline receipt bytes or PDF text extraction when the MCP server filesystem is not under direct user control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool call recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Splitwise account data, balances, record identifiers, receipt bytes, extracted receipt text, or receipt file paths returned by the MCP server.]

## Skill Version(s):

2.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
