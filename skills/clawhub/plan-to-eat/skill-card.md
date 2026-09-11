## Description:

This skill helps an agent use the connected plan-to-eat MCP server to view and update a user's Plan to Eat recipes, meal planner, freezer, and shopping list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-zwingli](https://clawhub.ai/user/alex-zwingli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to manage a Plan to Eat account through a connected MCP server, including meal planning, recipe lookup, freezer tracking, and shopping-list updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Plan to Eat credentials and identifies the password as the primary environment variable.

Mitigation: Provide credentials through the host environment, never paste the password into chat, and limit access to shells or hosts that can read those variables.

Risk: The connected MCP server gives the agent read and write access to recipes, the meal planner, freezer entries, and the shopping list.

Mitigation: Review planned changes before execution and confirm destructive or account-changing actions such as deleting planner events or modifying shopping-list rows.

Risk: The optional session cache can persist account access on disk.

Mitigation: Disable the cache by setting PLAN_TO_EAT_SESSION_FILE to an empty value or protect the cache path on shared machines.

Risk: Installation depends on a third-party npm package.

Mitigation: Keep install commands pinned to version 0.7.3 and verify npm signatures or provenance where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alex-zwingli/skills/plan-to-eat)
- [plan-to-eat-mcp homepage](https://github.com/alex-zwingli/plan-to-eat-mcp)
- [plan-to-eat-mcp npm package](https://www.npmjs.com/package/plan-to-eat-mcp)
- [plan-to-eat-mcp tool reference](https://github.com/alex-zwingli/plan-to-eat-mcp/blob/main/docs/TOOLS.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with MCP tool-call examples and bash setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured plan-to-eat MCP server and user-supplied Plan to Eat credentials.]

## Skill Version(s):

0.7.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
