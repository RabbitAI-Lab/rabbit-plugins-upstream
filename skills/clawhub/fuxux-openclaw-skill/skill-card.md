## Description:

Helps OpenClaw agents draft, schedule, publish, and manage social posts across Fuxux-connected platforms using REST or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abogitoff](https://clawhub.ai/user/abogitoff)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and creators use this skill to prepare drafts, schedule and publish posts, review publishing status and analytics, and manage content on Fuxux-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Fuxux API key can allow access to connected social accounts and posting tools.

Mitigation: Keep FUXUX_API_KEY secret, do not commit it, and rotate it if exposed.

Risk: Unreviewed or bulk publishing and deletion can cause unwanted public posts or lost Fuxux records.

Mitigation: Use drafts for review and confirm mass posting or deletion before execution.

Risk: The MCP example runs the mcp-remote package through npx.

Mitigation: Vet or pin mcp-remote before using the MCP example.

## Reference(s):

- [Fuxux OpenClaw integration](https://www.fuxux.com/openclaw)
- [Fuxux API reference](https://www.fuxux.com/reference)
- [Fuxux OpenAPI specification](https://www.fuxux.com/openapi.json)
- [Fuxux MCP setup](https://www.fuxux.com/mcp/docs)
- [ClawHub skill listing](https://clawhub.ai/abogitoff/skills/fuxux-openclaw-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with API examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for drafts, publishing, scheduling, account management, and analytics.]

## Skill Version(s):

1.1.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
