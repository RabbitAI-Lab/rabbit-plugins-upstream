## Description:

Build, harden, and debug production MCP servers with the TypeScript SDK, covering transports, tool schemas, results, errors, OAuth, token budgets, SDK migration, MCP Apps, extensions, and Registry usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill as a decision reference when writing, reviewing, hardening, debugging, or migrating production MCP servers and their tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP security guidance is advisory and may include an internally inconsistent Origin-header note.

Mitigation: Double-check security-critical requirements, especially browser-accessible server Origin handling, against the official MCP specification before production implementation.

Risk: Generated recommendations can change MCP server behavior even though the skill itself is documentation-only.

Mitigation: Review proposed code, configuration, and migration changes before applying them to deployed servers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/mcp-best-practices)
- [Source homepage](https://github.com/tenequm/skills/tree/main/skills/mcp-best-practices)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [TypeScript SDK documentation](https://ts.sdk.modelcontextprotocol.io)
- [MCP Inspector documentation](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)
- [MCP conformance suite](https://github.com/modelcontextprotocol/conformance)
- [Transport Patterns](references/transport-patterns.md)
- [Tool Schema Guide](references/tool-schema-guide.md)
- [Security and Authorization](references/security-auth.md)
- [Error Handling](references/error-handling.md)
- [Spec 2026-07-28](references/spec-2026-07-28.md)
- [V2 Migration](references/v2-migration.md)
- [MCP Apps](references/mcp-apps.md)
- [Extensions and Registry](references/extensions-registry.md)
- [Known SDK Bugs](references/sdk-bugs.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline TypeScript and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; no automatic execution, persistence, or hidden data access.]

## Skill Version(s):

1.1.1 (source: SKILL.md metadata, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
