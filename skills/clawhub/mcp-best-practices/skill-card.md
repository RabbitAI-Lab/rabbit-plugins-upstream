## Description: <br>
Build, secure, and optimize production MCP servers with the TypeScript SDK, covering transports, tool and schema design, error handling, security and OAuth, performance, known SDK issues, content delivery, v2 migration, MCP Apps, extensions, and the Registry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineers use this skill when building or reviewing production MCP servers and tools. It helps them make implementation decisions about transports, tool schemas, result delivery, error handling, OAuth security, performance, v2 migration, apps, extensions, and registry integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may copy guidance into production MCP servers without adapting it to their threat model. <br>
Mitigation: Review the guidance against the deployment environment and add authentication, origin validation, least-privilege scopes, rate limiting, and explicit GET /mcp handling before public exposure. <br>
Risk: The skill is a documentation reference rather than an enforcement mechanism. <br>
Mitigation: Use it to inform implementation and review decisions, then validate the resulting server with security review, tests, and deployment-specific controls. <br>
Risk: License evidence is inconsistent between server metadata and the artifact license file. <br>
Mitigation: Confirm the intended release license before publishing or redistributing the skill card. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/tenequm/skills/mcp-best-practices) <br>
- [Source homepage](https://github.com/tenequm/skills/tree/main/skills/mcp-best-practices) <br>
- [Error Handling](references/error-handling.md) <br>
- [Extensions and Registry](references/extensions-registry.md) <br>
- [MCP Apps](references/mcp-apps.md) <br>
- [Security and Authorization](references/security-auth.md) <br>
- [Tool Schema Guide](references/tool-schema-guide.md) <br>
- [Transport Patterns](references/transport-patterns.md) <br>
- [V2 Migration Guide](references/v2-migration.md) <br>
- [MCP latest specification](https://modelcontextprotocol.io/specification/latest) <br>
- [MCP TypeScript SDK docs](https://ts.sdk.modelcontextprotocol.io) <br>
- [MCP TypeScript SDK v2 docs](https://ts.sdk.modelcontextprotocol.io/v2/) <br>
- [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) <br>
- [MCP Registry](https://modelcontextprotocol.io/registry/about) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with TypeScript examples, command snippets, tables, and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only reference material; no code is installed or executed by the skill itself.] <br>

## Skill Version(s): <br>
0.8.2 (source: frontmatter, changelog, and server release metadata; released 2026-07-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
