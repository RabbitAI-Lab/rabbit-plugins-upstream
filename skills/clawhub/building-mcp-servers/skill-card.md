## Description:

Use when building a new MCP server in TypeScript, Python, or C# that exposes tools to LLMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, implement, test, secure, and evaluate MCP servers for TypeScript, Python, and C# integrations that expose tools, resources, and prompts to LLM clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-paste examples may run unpinned packages or fetch tooling at runtime.

Mitigation: Pin package versions, verify packages on the official registry, and avoid runtime npx downloads before installing or using generated commands.

Risk: Example servers may expose unauthenticated network services or bind beyond local development scope.

Mitigation: Bind local development servers to 127.0.0.1 and add authentication before using remote MCP transports.

Risk: Filesystem resource examples could expose local files if paths are not constrained.

Mitigation: Validate filesystem resource paths against a fixed root and return only the data promised by the tool contract.

Risk: Credentials could be exposed in examples, schemas, tests, or command-line arguments.

Mitigation: Use environment variables or secret managers and avoid placing API keys, bearer tokens, or credentials directly in tool schemas, examples, tests, or command-line arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/building-mcp-servers)
- [Metadata repository URL](https://github.com/afonsoft/skills)
- [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- [MCP authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [MCP Server Best Practices](references/mcp_best_practices.md)
- [Node/TypeScript MCP Server Implementation Guide](references/node_mcp_server.md)
- [Python MCP Server Implementation Guide](references/python_mcp_server.md)
- [.NET/C# MCP Server Implementation Guide](references/dotnet_mcp_server.md)
- [Quick Start: Language Implementations](references/quick-start.md)
- [Transport, Authentication, and Migration](references/transport-and-auth.md)
- [MCP Server Evaluation Guide](references/evaluation.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code blocks, shell commands, configuration examples, and evaluation XML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include language-specific MCP server scaffolding, tool schemas, transport and authentication guidance, test steps, and evaluation questions.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata; artifact metadata version 1.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
