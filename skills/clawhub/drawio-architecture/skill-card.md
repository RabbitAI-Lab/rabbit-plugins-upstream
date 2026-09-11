## Description:

Generates editable draw.io/diagrams.net architecture, system, network, cloud, flowchart, ER, UML, and C4-style diagrams, and guides agents through draw.io MCP setup or local draw.io export workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create professional draw.io architecture and systems diagrams, configure the official draw.io MCP server for supported agent clients, or export and validate local .drawio deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled setup helper can persist an unpinned remote MCP command and may write broader user-level configuration than expected.

Mitigation: Do not run the setup helper or Cursor one-click install as-is; manually configure a reviewed, exact @drawio/mcp@VERSION entry and prefer workspace-scoped configuration.

Risk: Hosted draw.io MCP use can send diagram XML to the hosted draw.io endpoint.

Mitigation: Use the hosted endpoint only for non-sensitive diagrams; prefer local stdio MCP or a trusted self-hosted DRAWIO_BASE_URL for sensitive architecture content.

Risk: MCP configuration files may expose local configuration details if copied into shared logs or tickets.

Mitigation: Avoid printing full MCP config files in shared locations and review configuration before sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/drawio-architecture)
- [Afonsoft Skills Repository](https://github.com/afonsoft/skills)
- [draw.io MCP Repository](https://github.com/jgraph/drawio-mcp)
- [draw.io MCP Server Documentation](https://www.drawio.com/docs/manual/generate/drawio-mcp-server/)
- [npm @drawio/mcp Package](https://www.npmjs.com/package/@drawio/mcp)
- [Agents365 drawio-skill Source](https://github.com/Agents365-ai/drawio-skill)
- [scarr05 claude-skills-pub Source](https://github.com/scarr05/claude-skills-pub)
- [Usage Guide](references/usage-guide.md)
- [MCP Server Configuration](references/mcp-config.md)
- [MCP Tools Reference](references/mcp-tools-reference.md)
- [Architecture Diagram Patterns](references/architecture-patterns.md)
- [Cloud Provider Icons](references/cloud-icons.md)
- [Style Guide](references/style-guide.md)
- [Usage Examples](references/usage-examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with XML, Mermaid, CSV, JSON configuration, shell command blocks, MCP tool calls, and optional .drawio file content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP use requires Node.js and npx; local image export requires the draw.io desktop CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
