## Description:

Access Splitwise expense and group data via MCP for expense, group, friend, balance, receipt, and shared-expense management tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users with a configured Splitwise MCP server use this skill to query Splitwise data and manage shared expenses, groups, friends, receipts, and balances through agent-driven tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced MCP server can change Splitwise account data, and the full server tool surface may be broader than the skill document clearly lists.

Mitigation: Review the complete MCP tool list before installation and require dry-run review before confirming expense, group, friend, profile, or comment changes.

Risk: The Splitwise API key grants account access to every request made through the server.

Mitigation: Protect SPLITWISE_API_KEY as a secret and avoid sharing logs, configs, or environments that expose it.

Risk: Receipt downloads may write files to the server filesystem, which can be confusing in hosted or containerized deployments.

Mitigation: Set SPLITWISE_OUTPUT_DIR explicitly or use write:false, inline:true, or extract_text:true when filesystem access is not appropriate.

Risk: Using an unpinned npm install can change the server code installed by npx over time.

Mitigation: Pin the npm package version for repeatable deployments.

## Reference(s):

- [Splitwise MCP npm package](https://www.npmjs.com/package/splitwise-mcp)
- [Splitwise app registration](https://secure.splitwise.com/apps/register)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Splitwise account data, filesystem paths for downloaded receipts, inline receipt bytes, or extracted PDF text depending on the selected MCP tool options.]

## Skill Version(s):

2.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
