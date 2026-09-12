## Description:

Use when building a new MCP server in TypeScript, Python, or C# that exposes tools to LLMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, implement, test, and evaluate MCP servers in TypeScript, Python, or C# that expose well-designed tools to LLM agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-paste examples could expose unauthenticated MCP servers.

Mitigation: Add authentication before remote exposure and bind local quick-start servers to 127.0.0.1.

Risk: Unpinned package installation or unreviewed npx execution could pull unexpected code.

Mitigation: Pin package versions, verify packages on official registries, and review commands before execution.

Risk: File-backed resources could read outside their intended scope.

Mitigation: Canonicalize paths and enforce containment checks before reading files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/building-mcp-servers)
- [Publisher metadata URL](https://github.com/afonsoft/skills)
- [MCP Server Best Practices](./references/mcp_best_practices.md)
- [Node/TypeScript MCP Server Implementation Guide](./references/node_mcp_server.md)
- [Python MCP Server Implementation Guide](./references/python_mcp_server.md)
- [.NET/C# MCP Server Implementation Guide](./references/dotnet_mcp_server.md)
- [Quick Start: Language Implementations](./references/quick-start.md)
- [Transport, Authentication, and Migration](./references/transport-and-auth.md)
- [MCP Server Evaluation Guide](./references/evaluation.md)
- [Official MCP documentation](https://modelcontextprotocol.io/)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code blocks and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP server scaffolding, transport setup, authentication guidance, tests, evaluation XML, and dependency pinning recommendations.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
