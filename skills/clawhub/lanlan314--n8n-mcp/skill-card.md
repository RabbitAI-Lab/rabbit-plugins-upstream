## Description:

通过 n8n MCP server (http://localhost:5678/mcp-server/http) 用 n8n Workflow SDK 创建、校验、发布和管理工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to create, validate, inspect, publish, execute, update, unpublish, and archive workflows in a local n8n instance through its MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform state-changing workflow actions, including create, update, publish, execute, unpublish, and archive.

Mitigation: Require explicit approval before state-changing MCP tool calls and validate workflow code before creation or update.

Risk: The n8n MCP token grants workflow administration access.

Mitigation: Keep the token secret and provide it only through approved n8n MCP configuration or secret handling.

Risk: Workflow code can automate external actions or process sensitive data.

Mitigation: Review node definitions, connections, schedules, credentials, and external endpoints before publishing or executing workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lanlan314/skills/n8n-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and TypeScript workflow code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include n8n MCP requests and workflow SDK code that require a user-provided n8n MCP token.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
