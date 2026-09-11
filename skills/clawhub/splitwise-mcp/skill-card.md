## Description:

Access Splitwise expense and group data via MCP for reading balances, groups, friends, receipts, notifications, categories, and currencies, and for creating, editing, deleting, restoring, or commenting on Splitwise records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to connect an agent to a registered Splitwise MCP server so it can answer questions about shared expenses and perform user-confirmed expense, group, friend, receipt, and comment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can create, update, delete, restore, and change membership for Splitwise resources tied to the configured account.

Mitigation: Require explicit user confirmation before any write, restore, delete, or membership-changing action, and review the exact group, user, amount, currency, and split details before execution.

Risk: Setup examples use an unpinned npx package install and a plaintext long-lived Splitwise API key.

Mitigation: Pin and review the splitwise-mcp package before installation, keep SPLITWISE_API_KEY out of source control, and restrict local file permissions for any config or environment files that contain it.

Risk: Receipt retrieval can write files on the MCP server host, which may expose sensitive receipt data or place files somewhere the user cannot access.

Mitigation: Use inline: true or extract_text: true unless host-side file output is intended, and set output_dir deliberately when files must be written.

## Reference(s):

- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Splitwise account data, write receipt files on the MCP server host, or return receipt bytes/text depending on tool parameters.]

## Skill Version(s):

2.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
