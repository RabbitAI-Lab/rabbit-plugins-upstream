## Description:

Build, harden, and debug production MCP servers with the TypeScript SDK, including transport choices, tool schemas, errors, OAuth, token budgets, SDK migration, MCP Apps, extensions, and registry guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill when writing or reviewing production MCP servers that already exist. It helps them choose transports, design tool schemas and results, handle errors, add OAuth, reduce token bloat, and migrate SDK or protocol versions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tunnel or MCP Apps examples can expose unintended tools or data if adapted without access controls.

Mitigation: Expose only intended tools, require authentication for remote access, avoid sensitive test data, and validate authorization server-side.

Risk: Security-sensitive implementation guidance may be copied into production without matching the deployment context.

Mitigation: Treat examples as design references and review the final server behavior against the security and authorization guidance before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/mcp-best-practices)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/mcp-best-practices)
- [Error Handling](references/error-handling.md)
- [Extensions and Registry](references/extensions-registry.md)
- [MCP Apps](references/mcp-apps.md)
- [Known SDK Bugs](references/sdk-bugs.md)
- [Security and Authorization](references/security-auth.md)
- [Spec 2026-07-28](references/spec-2026-07-28.md)
- [Tool Schema Guide](references/tool-schema-guide.md)
- [Transport Patterns](references/transport-patterns.md)
- [V2 Migration Guide](references/v2-migration.md)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [TypeScript SDK documentation](https://ts.sdk.modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with TypeScript snippets, command examples, configuration notes, and reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only output; may include MCP version, SDK version, and environment variable guidance.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter, CHANGELOG.md, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
