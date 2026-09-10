## Description:

Use when generating draw.io or diagrams.net architecture diagrams, network topologies, cloud diagrams, flowcharts, ER diagrams, and related visualizations, including MCP setup and editable .drawio XML authoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create editable architecture and systems diagrams, configure draw.io MCP integrations, and produce local draw.io deliverables when MCP is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can persistently add an unpinned remote MCP package to agent configuration.

Mitigation: Review configuration diffs before applying them and use a verified pinned @drawio/mcp@<VERSION> package.

Risk: Dry-run or configuration output may expose existing config contents.

Mitigation: Avoid sharing setup output from environments whose MCP configs may contain tokens or private server settings.

Risk: Hosted draw.io MCP endpoints receive diagram XML.

Mitigation: Use local stdio or a trusted self-hosted draw.io instance for confidential or regulated architecture diagrams.

## Reference(s):

- [draw.io MCP documentation](https://www.drawio.com/docs/manual/generate/drawio-mcp-server/)
- [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp)
- [draw.io MCP npm package](https://www.npmjs.com/package/@drawio/mcp)
- [afonsoft/skills](https://github.com/afonsoft/skills)
- [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill)
- [scarr05/claude-skills-pub](https://github.com/scarr05/claude-skills-pub)
- [Architecture diagram patterns](references/architecture-patterns.md)
- [MCP server configuration](references/mcp-config.md)
- [MCP tools reference](references/mcp-tools-reference.md)
- [Usage guide](references/usage-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with XML, JSON, Mermaid, CSV, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce editable .drawio XML, MCP tool calls, MCP client configuration blocks, viewer URLs, and local export instructions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
