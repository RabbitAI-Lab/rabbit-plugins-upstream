## Description:

Access Splitwise expense and group data via MCP for expense, group, friend, balance, and shared-expense management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Splitwise through an MCP server, inspect expenses, groups, friends, balances, notifications, categories, and currencies, and propose expense or group changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can use a Splitwise API key to read financial, group, friend, and email data.

Mitigation: Install only when that data access is acceptable, protect the API key, and keep it out of prompts, logs, and shared configuration.

Risk: The installed MCP package exposes high-impact account, profile, friend, group, comment, and expense mutation tools that are not fully disclosed by the skill document.

Mitigation: Review the live tool list after installation and require explicit user confirmation before any write or delete action.

## Reference(s):

- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide MCP calls that read or mutate Splitwise account, friend, group, comment, and expense data.]

## Skill Version(s):

2.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
