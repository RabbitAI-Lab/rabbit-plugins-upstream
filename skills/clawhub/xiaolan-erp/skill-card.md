## Description:

小蓝进销存 is an ERP connector for inventory, purchasing, sales, cost accounting, and reporting through AI-driven conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lan202509](https://clawhub.ai/user/lan202509)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators and agents use this skill to configure and operate a remote ERP service for warehouses, items, suppliers, customers, purchasing, sales, inventory checks, and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs the agent to modify MCP client configuration.

Mitigation: Require the agent to show and obtain user confirmation before writing any MCP configuration changes.

Risk: The skill can persist ERP bearer tokens that grant access to business data.

Mitigation: Treat generated tokens as sensitive credentials and require user confirmation before storing or changing them.

## Reference(s):

- [Xiaolan ERP MCP Endpoint](https://xiaolan-tech.com/mcp/erp)
- [ClawHub Skill Page](https://clawhub.ai/lan202509/skills/xiaolan-erp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON MCP configuration snippets and natural-language ERP workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP client configuration snippets and bearer token handling guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
