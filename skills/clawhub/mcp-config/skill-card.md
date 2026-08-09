## Description:

mcp-config helps agents add, move, format, catalog, and troubleshoot MCP server configurations across supported coding agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to configure MCP servers, choose the right scope for a server entry, move existing entries between scopes, and diagnose connection failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PostgreSQL MCP examples may encourage unrestricted database access or inline credential handling.

Mitigation: Review database examples before use, prefer read-only or least-privilege credentials, avoid committing secrets to project `.mcp.json`, and keep sensitive MCP servers in local or user scope when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/mcp-config)
- [Add MCP Server](artifact/add.md)
- [MCP Server Catalog](artifact/catalog.md)
- [MCP Server Connection Diagnostics](artifact/diagnostics.md)
- [MCP Server Format](artifact/format.md)
- [Move MCP Server](artifact/move.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include agent-specific MCP configuration steps, validation checks, and troubleshooting commands.]

## Skill Version(s):

0.3.1 (source: release evidence and CHANGELOG, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
