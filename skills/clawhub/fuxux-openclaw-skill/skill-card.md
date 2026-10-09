## Description:

Helps OpenClaw agents draft, schedule, publish, and manage social content across 12 platforms through Fuxux.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abogitoff](https://clawhub.ai/user/abogitoff)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and teams use this skill with OpenClaw to prepare platform-specific captions, manage drafts and schedules, publish content, and review publishing analytics for Fuxux-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with the Fuxux API key can publish, schedule, edit, or delete managed posts.

Mitigation: Review generated content and connected accounts before broad posting, and confirm destructive actions.

Risk: Exposure of the FUXUX_API_KEY could grant access to connected social accounts.

Mitigation: Keep the key private and rotate it if exposed.

Risk: The example MCP bridge installs an unpinned Node package.

Mitigation: Review and pin the bridge package version before using the example configuration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/abogitoff/skills/fuxux-openclaw-skill)
- [Fuxux OpenClaw guide](https://www.fuxux.com/openclaw)
- [Fuxux API reference](https://www.fuxux.com/reference)
- [Fuxux OpenAPI specification](https://www.fuxux.com/openapi.json)
- [Fuxux MCP setup guide](https://www.fuxux.com/mcp/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with HTTP and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.1.5 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
