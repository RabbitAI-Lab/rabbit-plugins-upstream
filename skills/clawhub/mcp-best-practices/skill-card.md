## Description:

Build, harden, and debug production MCP servers with the TypeScript SDK. Use when writing or reviewing an MCP server - transports, tool schemas, errors, OAuth, token bloat, SDK migrations, MCP Apps, Registry. Assumes a server already exists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill as a decision reference when writing or reviewing production MCP servers with the TypeScript SDK, especially for transport choices, tool schemas, error handling, OAuth, server hardening, token budgets, SDK migrations, MCP Apps, and registry behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Developer examples may be copied into a production MCP server without review.

Mitigation: Review examples before reuse, pin dependency versions, and use lockfiles.

Risk: MCP tools that fetch arbitrary URLs can create SSRF exposure.

Mitigation: Add SSRF protections before implementing arbitrary URL fetch tools.

Risk: Exposing local MCP endpoints through a tunnel can make private tooling reachable by unintended users.

Mitigation: Add appropriate authentication and authorization before exposing local endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/mcp-best-practices)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/mcp-best-practices)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [TypeScript SDK documentation](https://ts.sdk.modelcontextprotocol.io)
- [MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)
- [MCP Registry](https://modelcontextprotocol.io/registry/about)
- [Conformance suite](https://github.com/modelcontextprotocol/conformance)
- [Tool Schema Guide](references/tool-schema-guide.md)
- [Spec 2026-07-28](references/spec-2026-07-28.md)
- [Transport Patterns](references/transport-patterns.md)
- [Security and Authorization](references/security-auth.md)
- [Known SDK Bugs](references/sdk-bugs.md)
- [V2 Migration Guide](references/v2-migration.md)
- [Error Handling](references/error-handling.md)
- [Extensions and Registry](references/extensions-registry.md)
- [MCP Apps](references/mcp-apps.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only decision reference; includes result-size budget guidance involving MAX_MCP_OUTPUT_TOKENS.]

## Skill Version(s):

1.2.1 (source: SKILL.md frontmatter and CHANGELOG, released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
