## Description:

Helps an OpenClaw agent draft, schedule, publish, edit, and review social posts across 13 platforms through Fuxux's API or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abogitoff](https://clawhub.ai/user/abogitoff)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and other Fuxux users can have an agent prepare platform-specific posts, save drafts, schedule or publish content, and inspect queues and publishing analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with Fuxux access can publish, edit, or delete social content on connected accounts.

Mitigation: Use draft mode when review is needed and confirm bulk or irreversible actions before execution.

Risk: Exposure of the Fuxux API key could allow unauthorized access to connected social accounts.

Mitigation: Keep FUXUX_API_KEY private and use an environment-based authorization header where supported.

Risk: MCP setup may install a remotely fetched bridge package.

Mitigation: Consider pinning mcp-remote to a reviewed version before connecting it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/abogitoff/skills/fuxux-openclaw-skill)
- [Fuxux OpenClaw guide](https://www.fuxux.com/openclaw)
- [Fuxux API reference](https://www.fuxux.com/reference)
- [Fuxux MCP setup](https://www.fuxux.com/mcp/docs)
- [Fuxux OpenAPI specification](https://www.fuxux.com/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-specific captions, posting instructions, and status or analytics summaries as requested.]

## Skill Version(s):

1.1.4 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
