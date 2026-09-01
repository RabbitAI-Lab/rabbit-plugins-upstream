## Description:

Build and configure Cargo AI agents, including prompts, model settings, RAG resources, MCP connections, memories, and deployments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create, configure, connect, and deploy Cargo AI agents through the Cargo CLI. It helps manage agent releases, knowledge attachments, MCP server/client setup, templates, model settings, and memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide write operations that change Cargo agents, releases, MCP settings, memories, and related workspace resources.

Mitigation: Review write commands before execution and confirm the active workspace with `cargo-ai whoami`.

Risk: API tokens and MCP connections can expose or extend workspace access.

Mitigation: Use appropriate token scopes, avoid unnecessary token sharing, and review MCP connection settings before deployment.

Risk: Lead and contact research workflows may involve personal or business data.

Mitigation: Ensure research and enrichment workflows comply with organizational policies, platform terms, and applicable privacy laws.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Agent examples](references/examples/agents.md)
- [MCP server examples](references/examples/mcp-servers.md)
- [AI template examples](references/examples/templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally return JSON and may require Cargo authentication.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
