## Description:

Use when building MCP (Model Context Protocol) servers that let LLMs call external APIs or services, in TypeScript (MCP SDK), Python (FastMCP), or C# (ModelContextProtocol.AspNetCore). Covers tool design, transports (Streamable HTTP/stdio), OAuth 2.1 auth, and evaluations. Do NOT use for consuming or configuring an existing MCP server, or for non-MCP API integrations. Part of the afonsoft/skills collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, implement, secure, and evaluate MCP servers that expose external APIs or services to LLM agents across TypeScript, Python, and .NET stacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated MCP servers may expose unauthenticated HTTP transports if examples are copied directly.

Mitigation: Prefer stdio or localhost during development, and add authentication plus Origin and Host validation before exposing HTTP transports.

Risk: Generated file-resource examples may allow unsafe local-file access.

Mitigation: Use path canonicalization, directory containment checks, and scoped access controls before using file-resource patterns.

Risk: Generated service tools may overexpose sensitive actions or data.

Mitigation: Enforce scopes inside sensitive tools, validate inputs at the boundary, and avoid returning secrets or raw internal API responses.

Risk: Unpinned dependencies can drift after code generation.

Mitigation: Pin package versions and verify packages against official npm, PyPI, or NuGet registries before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/building-mcp-servers)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- [MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [TypeScript MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [C# MCP SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [MCP Server Best Practices](references/mcp_best_practices.md)
- [Node/TypeScript MCP Server Implementation Guide](references/node_mcp_server.md)
- [Python MCP Server Implementation Guide](references/python_mcp_server.md)
- [.NET/C# MCP Server Implementation Guide](references/dotnet_mcp_server.md)
- [Transport, Authentication, and Migration](references/transport-and-auth.md)
- [MCP Server Evaluation Guide](references/evaluation.md)
- [Quick Start: Language Implementations](references/quick-start.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks and implementation checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated MCP server code, dependency installation commands, transport configuration, authentication guidance, and evaluation XML examples.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
