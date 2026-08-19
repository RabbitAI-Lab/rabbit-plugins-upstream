## Description:

MCP server configuration and diagnostics guidance for adding, moving, formatting, cataloging, and troubleshooting MCP server entries across supported agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to configure MCP servers, choose the right scope, validate agent-specific configuration formats, and diagnose connection failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PostgreSQL MCP examples may encourage unrestricted database access or inline credentials.

Mitigation: Review PostgreSQL entries before copying them, prefer read-only or least-privilege database access, avoid unrestricted mode unless intentionally needed, and keep credentials out of committed configs and screenshots.

Risk: Global MCP entries can change agent behavior across projects.

Mitigation: Confirm scope and target agents before adding global entries, and choose the narrowest scope that meets the user's need.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/mcp-config)
- [Add MCP Server](add.md)
- [Move MCP Server](move.md)
- [MCP Server Format](format.md)
- [MCP Server Catalog](catalog.md)
- [MCP Server Connection Diagnostics](diagnostics.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-directed setup and troubleshooting guidance; no autonomous execution is implied.]

## Skill Version(s):

0.3.2 (source: server release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
