## Description:

Guides agents in reading, updating, and optionally automating Notion workspaces through a managed Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using an agent to find Notion content, manage pages and databases, or set up approved Notion automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access or change content in the connected Notion workspace.

Mitigation: Approve connections and each write, use the minimum required access, and specify the exact connection and target page or database.

Risk: Enabled functions, triggers, destinations, or local event handlers can continue running and forward future event data.

Mitigation: Review and explicitly approve automation before enabling it; restrict destinations and disable automations that are no longer needed.

## Reference(s):

- [Notion MCP skill release](https://clawhub.ai/byungkyu/skills/notion-mcp)
- [Maton](https://maton.ai)
- [Notion MCP overview](https://developers.notion.com/guides/mcp)
- [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Maton documentation](https://docs.maton.ai)
- [Notion event triggers](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Notion actions require an authorized connection; writes require user confirmation.]

## Skill Version(s):

1.2.5 (source: server-resolved release; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
