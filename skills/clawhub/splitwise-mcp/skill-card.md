## Description:

Access Splitwise expense, group, friend, receipt, notification, category, and currency data through an MCP server, including creating, editing, deleting, and restoring expenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Splitwise for natural-language expense tracking, group management, balance lookup, and receipt retrieval. It is intended for environments where the splitwise-mcp server is installed and registered with a Splitwise API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable account-changing Splitwise actions such as expense creation, expense edits, soft deletion, restoration, and group membership changes.

Mitigation: Review account-changing actions before execution, especially target groups, users, dates, amounts, and deletion or restoration requests.

Risk: Receipt retrieval may expose sensitive financial details or write receipt files to the server filesystem.

Mitigation: Configure receipt output to a controlled directory, or use inline bytes or PDF text extraction when hosted storage paths are not directly readable.

Risk: The Splitwise API key grants access to personal expense and group data.

Mitigation: Store the API key as a secret, limit access to the MCP configuration, and install the skill only where Splitwise data access is intended.

## Reference(s):

- [splitwise-mcp ClawHub page](https://clawhub.ai/chrischall/skills/splitwise-mcp)
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp)
- [splitwise-mcp source repository](https://github.com/chrischall/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, bash, and MCP tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Splitwise account reads and account-changing actions through the configured MCP server.]

## Skill Version(s):

2.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
