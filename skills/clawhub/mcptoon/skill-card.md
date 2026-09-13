## Description:

Compress MCP tool discovery with the mcptoon CLI for sessions with large MCP tool catalogs, token-cost concerns, or cross-agent MCP server configuration needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect, search, and call MCP tools through a compact mcptoon manifest instead of loading large raw tool schemas into context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable external installs may change behavior after review.

Mitigation: Review the mcptoon package and marketplace plugin before installation, avoid automatic upgrades, and prefer a pinned reviewed version.

Risk: MCP bridge configuration may route agent tool calls through unintended servers.

Mitigation: Inspect any MCP bridge or .mcp.json changes and connect mcptoon only to MCP servers the deployment intends it to mediate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/activeing123/skills/mcptoon)
- [Publisher profile](https://clawhub.ai/user/activeing123)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, command arguments, and setup steps for the mcptoon CLI or bridge.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
