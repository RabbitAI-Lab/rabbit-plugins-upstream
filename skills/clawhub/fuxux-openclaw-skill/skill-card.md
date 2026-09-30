## Description:

Guides an OpenClaw agent in managing Fuxux social posts across connected platforms, including drafts, scheduling, publishing, analytics, and AI caption generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abogitoff](https://clawhub.ai/user/abogitoff)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and teams use this skill to direct an agent to draft, schedule, publish, edit, and review posts across their connected Fuxux accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with the Fuxux API key can manage connected social accounts and publish unintended content.

Mitigation: Keep the key private and use drafts or scheduled posts for review before publishing.

Risk: Bulk posting or deletion can have unintended or irreversible effects.

Mitigation: Confirm bulk and irreversible actions with the user before executing them.

Risk: Installing mcp-remote without a pinned version may not meet strict dependency-control requirements.

Mitigation: Pin or preinstall mcp-remote where dependency control is required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/abogitoff/skills/fuxux-openclaw-skill)
- [Fuxux OpenClaw guide](https://www.fuxux.com/openclaw)
- [Fuxux API reference](https://www.fuxux.com/reference)
- [Fuxux MCP setup](https://www.fuxux.com/mcp/docs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated Fuxux actions that create, schedule, edit, or delete posts.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
