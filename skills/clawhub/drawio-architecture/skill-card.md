## Description:

Use when generating or editing draw.io/diagrams.net architecture diagrams via MCP or native XML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, edit, validate, and deliver editable draw.io architecture, system, network, cloud, flowchart, ER, UML, and C4-style diagrams through MCP tools or local draw.io XML and CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup helper can configure an unpinned @drawio/mcp package, which may execute whatever version npm resolves at runtime.

Mitigation: Manually add or edit the MCP configuration to use npx -y @drawio/mcp@<VERSION> after verifying the version and publisher.

Risk: The setup helper may persistently modify agent MCP configuration and can print existing configuration during dry runs.

Mitigation: Review changes locally, back up configuration files before writing, and do not paste dry-run output into logs or chats if it may contain secrets.

Risk: The hosted draw.io MCP endpoint receives diagram XML and may expose sensitive architecture details to the vendor endpoint.

Mitigation: Use local stdio MCP or a trusted self-hosted draw.io endpoint for sensitive or regulated diagrams; reserve the hosted endpoint for non-sensitive content.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/afonsoft/skills/drawio-architecture)
- [drawio MCP project](https://github.com/jgraph/drawio-mcp)
- [draw.io MCP server documentation](https://www.drawio.com/docs/manual/generate/drawio-mcp-server/)
- [@drawio/mcp npm package](https://www.npmjs.com/package/@drawio/mcp)
- [Agents365 drawio skill source](https://github.com/Agents365-ai/drawio-skill)
- [scarr05 Claude skills source](https://github.com/scarr05/claude-skills-pub)
- [MCP Server Configuration](references/mcp-config.md)
- [MCP Tools Reference](references/mcp-tools-reference.md)
- [Architecture Diagram Patterns](references/architecture-patterns.md)
- [Cloud Icons](references/cloud-icons.md)
- [Usage Guide](references/usage-guide.md)
- [Usage Examples](references/usage-examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with draw.io XML, Mermaid or CSV content, JSON configuration snippets, and bash commands when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MCP tool-call content for opening diagrams, local .drawio XML files, exported image/PDF instructions, and validation commands.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
