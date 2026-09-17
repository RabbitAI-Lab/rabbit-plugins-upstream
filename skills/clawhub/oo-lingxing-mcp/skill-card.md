## Description:

Operate Lingxing MCP through OOMOL's oo CLI to discover available Lingxing ERP MCP tools and call them with schema-checked JSON arguments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live Lingxing ERP MCP tool schemas and run selected actions through an OOMOL-connected Lingxing account. It supports read-oriented discovery and tool execution, with additional care required because called tools may create or update ERP data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Lingxing ERP data through called MCP tools, even though parts of its description emphasize searching and reading.

Mitigation: Inspect each tool's live schema and behavior annotations before execution, then confirm the exact effect and JSON payload with the user before running write-capable actions.

Risk: The first-time setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Avoid pipe-to-shell installation unless the OOMOL CLI installer source and integrity have been independently verified; prefer documented package or manual installation paths when available.

## Reference(s):

- [Lingxing MCP homepage](https://www.lingxing.com/help/article/mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lingxing-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before tool calls; command results include connector data and execution metadata.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
