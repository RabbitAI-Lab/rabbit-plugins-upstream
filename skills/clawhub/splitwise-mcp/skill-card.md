## Description:

Access Splitwise expense and group data via MCP, including reading balances, groups, friends, and expenses and adding, editing, or deleting expense records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect a configured Splitwise MCP server so users can query shared-expense data and perform account, group, friend, receipt, comment, and expense workflows through natural language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes Splitwise operations that can make real account, group, friend, comment, receipt, user, and expense changes.

Mitigation: Review requested actions before invoking write tools, scope the API key to the intended account, and reserve installation for agents trusted to manage Splitwise data.

Risk: Receipt download options can write files to the MCP server filesystem by default.

Mitigation: Prefer inline receipt bytes or PDF text extraction when filesystem access is not intended, and set an explicit output directory when writing files is necessary.

Risk: The ClawHub security verdict is suspicious because the account-changing surface is broader than the main description makes clear.

Mitigation: Review the full tool list and security guidance before installation, especially if the agent should have only expense-level access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MCP setup guidance and tool-use guidance; configured tool calls may read or change Splitwise account data and can download receipt files.]

## Skill Version(s):

3.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
