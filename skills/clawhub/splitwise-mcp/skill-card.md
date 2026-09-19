## Description:

Access Splitwise expense, group, friend, receipt, and balance data through an MCP server, including supported create, update, delete, and restore actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent query and manage Splitwise shared expenses, groups, friends, receipts, and balances through registered MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can create, update, delete, or restore Splitwise expenses and can modify groups, friends, comments, and profile data.

Mitigation: Require explicit user confirmation before any write, delete, restore, or profile-changing action.

Risk: The Splitwise API key grants account access to the MCP server.

Mitigation: Store SPLITWISE_API_KEY as a protected credential and avoid exposing it in prompts, logs, shared configuration, or committed files.

Risk: Receipt retrieval writes files to disk by default and returns server-side paths that may not be readable in hosted or containerized environments.

Mitigation: Use inline or text receipt retrieval unless file output is intentional, and set an explicit output directory when writing receipts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [npm package: splitwise-mcp](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with JSON configuration and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP tool results may include Splitwise records, action receipts, receipt text, receipt bytes, or server-side file paths depending on the selected tool options.]

## Skill Version(s):

3.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
