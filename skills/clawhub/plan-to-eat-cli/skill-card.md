## Description:

Use this skill when an agent needs to interact with Plan to Eat meal planning, recipes, planner entries, freezer items, and shopping lists through the plan-to-eat CLI when the MCP server is not connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-zwingli](https://clawhub.ai/user/alex-zwingli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent inspect and update Plan to Eat meal plans, recipes, freezer inventory, and shopping lists through shell commands when the structured MCP tools are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI needs access to Plan to Eat account credentials and may cache a local session file.

Mitigation: Use environment variables or a local .env file without pasting secrets into chat, and set PLAN_TO_EAT_SESSION_FILE to an empty value if a retained cookie file is not acceptable.

Risk: Using npx or npm executes the plan-to-eat-mcp package from the npm supply chain.

Mitigation: Use the pinned 0.7.3 install command, review the package when needed, and run npm signature checks before relying on an installation.

Risk: Planner and shopping-list write commands can make immediate changes and some operations have no dry-run.

Mitigation: Confirm destructive or user-visible changes before running them, and read back the affected planner or shopping-list state after writes.

## Reference(s):

- [Plan to Eat MCP project homepage](https://github.com/alex-zwingli/plan-to-eat-mcp)
- [Plan to Eat CLI tool reference](https://github.com/alex-zwingli/plan-to-eat-mcp/blob/main/docs/TOOLS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should use --json where supported and require Plan to Eat credentials plus Node with either plan-to-eat or npx available.]

## Skill Version(s):

0.7.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
