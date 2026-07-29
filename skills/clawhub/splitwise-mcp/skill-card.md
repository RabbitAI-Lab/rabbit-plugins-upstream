## Description: <br>
Access Splitwise expense, group, friend, balance, notification, category, and currency data through an MCP server, with tools to create, update, and delete expenses and manage group membership. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent answer Splitwise questions and perform account actions such as listing balances, creating expenses, editing expenses, deleting expenses, and managing group membership. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive personal and financial Splitwise data. <br>
Mitigation: Limit friend, group, notification, and expense listings to information needed for the user's current task. <br>
Risk: Create, edit, delete, and group-membership tools make real account changes. <br>
Mitigation: Require explicit user confirmation before using tools that change expenses or groups. <br>
Risk: Use requires a Splitwise API key and trust in the splitwise-mcp package. <br>
Mitigation: Install only from trusted sources and keep the Splitwise API key scoped and protected in environment configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/splitwise-mcp) <br>
- [splitwise-mcp npm package](https://www.npmjs.com/package/splitwise-mcp) <br>
- [Splitwise app registration](https://secure.splitwise.com/apps/register) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline JSON configuration and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger Splitwise MCP tool calls that read or modify account data.] <br>

## Skill Version(s): <br>
2.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
