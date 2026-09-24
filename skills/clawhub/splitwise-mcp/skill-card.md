## Description:

Access Splitwise expense and group data via MCP for questions about expenses, groups, friends, balances, and requests to add, edit, or delete expenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Splitwise MCP server for shared-expense workflows. It supports reading Splitwise account data and performing live expense, group, friend, comment, and receipt operations through MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live create, update, delete, restore, group membership, friend, and comment actions in Splitwise.

Mitigation: Require user confirmation before any write operation and review the target group, people, amount, split, and expense identifier before calling the tool.

Risk: The skill uses a Splitwise API key that can expose account data such as balances, emails, groups, receipts, and activity.

Mitigation: Keep the API key private, provide it only through the MCP server environment, and install the skill only when Splitwise account access is intended.

Risk: Receipt retrieval can write files on the MCP server filesystem.

Mitigation: Set an explicit output directory or use inline or text extraction modes when receipt files should not be written.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP tool calls that read Splitwise data, change live Splitwise records, or retrieve receipt files.]

## Skill Version(s):

3.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
