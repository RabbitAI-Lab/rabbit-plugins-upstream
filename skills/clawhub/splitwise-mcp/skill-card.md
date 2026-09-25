## Description:

splitwise-mcp helps agents access Splitwise expenses, groups, friends, balances, receipts, and expense-management actions through an MCP server backed by the Splitwise API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Splitwise MCP server for shared-expense workflows, including reading balances and groups, creating or editing expenses, managing friends or group membership, and retrieving receipt data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses a Splitwise API key and can access account data including expenses, groups, friends, balances, and receipts.

Mitigation: Install and configure it only when the user is comfortable granting that account access, and protect the SPLITWISE_API_KEY as a secret.

Risk: Write tools can create, edit, delete, or restore Splitwise records.

Mitigation: Review write previews and confirm only the intended changes before allowing write operations to proceed.

Risk: Receipt downloads or extracted receipt text can contain sensitive personal or financial information and may be written to disk.

Mitigation: Choose output directories deliberately, prefer inline or extracted-text modes when file access is constrained, and handle generated receipt files as sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Splitwise account data, expense records, group and friend data, balances, write confirmations, receipt paths, extracted receipt text, or inline receipt bytes depending on the MCP tool used.]

## Skill Version(s):

3.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
