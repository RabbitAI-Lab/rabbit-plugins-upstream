## Description:

Helps agents administer Cargo AI resources by creating and configuring agents, attaching retrieval knowledge, connecting MCP servers, managing memories, and deploying releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure Cargo AI agents, attach knowledge and MCP tools, manage release settings, and deploy agent changes in a Cargo workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide changes to live Cargo workspace AI resources, including agent updates, MCP server changes, memory edits, and release deployments.

Mitigation: Confirm the active workspace with cargo-ai whoami, verify UUIDs before write operations, and review deploy, remove, and direct API commands before execution.

Risk: MCP resource configuration can expose tools or data beyond the intended agent scope if configured too broadly.

Mitigation: Keep MCP resources read-only unless writes are required, disable unnecessary tools, and review the full actions and resources arrays before deploying changes.

## Reference(s):

- [Cargo Skills GitHub Repository](https://github.com/getcargohq/cargo-skills)
- [Response Shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Agent Examples](references/examples/agents.md)
- [MCP Server Examples](references/examples/mcp-servers.md)
- [AI Template Examples](references/examples/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally return JSON on stdout; failures return JSON with an errorMessage.]

## Skill Version(s):

2.3.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
