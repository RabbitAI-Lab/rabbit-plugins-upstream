## Description:

Read and manage a signed-in Skylight Calendar family hub, including calendar events, chores and rewards, shared lists, meal plans, media-related features, and frame settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP skill to let an agent read and update a Skylight family hub for household calendar, chores, lists, meals, media, and frame-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses persistent Skylight account credentials and may access private family information.

Mitigation: Review before installing, use project-local MCP configuration where possible, and limit credential exposure to trusted environments.

Risk: The connector exposes media upload, messages/photo albums, and frame/device/member settings in addition to calendar, chores, lists, and meals.

Mitigation: Treat those broader family-hub capabilities as in scope when deciding whether to enable the skill.

Risk: Some recurrence-scoped writes can affect more than the single occurrence named by the user.

Mitigation: Use the documented dry-run confirmation flow and only re-issue gated calls with confirmation after reviewing the affected scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON configuration examples and tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue MCP tool calls that read or modify Skylight account data after credentials are configured.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
