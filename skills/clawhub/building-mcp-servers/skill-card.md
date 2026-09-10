## Description:

Use when building MCP (Model Context Protocol) servers that let LLMs call external APIs or services, in TypeScript (MCP SDK), Python (FastMCP), or C# (ModelContextProtocol.AspNetCore).

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to plan, implement, test, and evaluate MCP servers that expose external APIs or services to LLM agents. It covers tool design, Streamable HTTP and stdio transports, OAuth 2.1 authentication, language-specific implementation patterns, and evaluation creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-ready server examples may expose unauthenticated MCP endpoints.

Mitigation: Add authentication and scope checks before exposing tools, and bind local HTTP servers to 127.0.0.1 unless remote access is intentionally secured.

Risk: Example commands or configuration can lead to credential mishandling.

Mitigation: Avoid putting real tokens in commands or config files; use environment variables or a secret manager.

Risk: Generated MCP server code may include unsafe dependency or input-handling choices.

Mitigation: Pin package versions, run package tools in an isolated development environment, validate file paths, and encode user-controlled URL parameters.

## Reference(s):

- [MCP Server Best Practices](references/mcp_best_practices.md)
- [Node/TypeScript MCP Server Implementation Guide](references/node_mcp_server.md)
- [Python MCP Server Implementation Guide](references/python_mcp_server.md)
- [.NET/C# MCP Server Implementation Guide](references/dotnet_mcp_server.md)
- [Quick Start: Language Implementations](references/quick-start.md)
- [Transport, Authentication, and Migration](references/transport-and-auth.md)
- [MCP Server Evaluation Guide](references/evaluation.md)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- [MCP Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Skill Metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code blocks, commands, configuration snippets, and XML evaluation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing development guidance for MCP server implementation and evaluation]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
