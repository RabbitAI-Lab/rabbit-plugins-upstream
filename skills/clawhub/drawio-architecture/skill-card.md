## Description:

Use when generating or editing draw.io/diagrams.net architecture diagrams via MCP or native XML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create editable architecture, system, cloud, network, flowchart, ER, UML, and C4-style diagrams in draw.io/diagrams.net. It supports MCP-based editor workflows, local draw.io XML authoring, and CLI export flows when image or document deliverables are needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup helper can persistently modify agent or IDE MCP configuration.

Mitigation: Inspect MCP configuration diffs before applying changes, use dry-run review carefully, and avoid the automated setup helper unless it is fixed.

Risk: The setup helper currently uses an unpinned npm command for @drawio/mcp.

Mitigation: Use only a pinned @drawio/mcp@<verified-version> entry and verify the package name and publisher before running it.

Risk: Existing MCP configuration contents may be printed during setup or dry-run output.

Mitigation: Do not paste dry-run output into shared logs when local MCP configuration may contain secrets.

Risk: The hosted draw.io endpoint receives diagram XML.

Mitigation: For sensitive diagrams, prefer local stdio with a trusted pinned package or a self-hosted draw.io instance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/drawio-architecture)
- [Artifact: SKILL.md](artifact/SKILL.md)
- [Usage Guide](artifact/references/usage-guide.md)
- [MCP Server Configuration](artifact/references/mcp-config.md)
- [MCP Tools Reference](artifact/references/mcp-tools-reference.md)
- [Architecture Patterns](artifact/references/architecture-patterns.md)
- [Cloud Icons](artifact/references/cloud-icons.md)
- [Usage Examples](artifact/references/usage-examples.md)
- [draw.io MCP documentation](https://www.drawio.com/docs/manual/generate/drawio-mcp-server/)
- [drawio-mcp repository](https://github.com/jgraph/drawio-mcp)
- [@drawio/mcp package](https://www.npmjs.com/package/@drawio/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with XML, Mermaid, CSV, JSON configuration, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce draw.io XML files, MCP tool payloads, viewer URLs, and export commands depending on the chosen delivery path.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
