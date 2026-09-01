## Description:

Read and manage a signed-in user's Skylight Calendar family hub, including calendar events, chores and reward stars, shared lists, meal plans, and frame-related account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read and update a Skylight family hub through the user's own signed-in Skylight account. It is suited for managing family calendars, chores, rewards, shared lists, meals, and related frame information from conversational requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires primary Skylight account credentials and can access sensitive family hub data.

Mitigation: Install only when that access is acceptable, keep configuration files out of source control and backups where possible, and restrict file permissions.

Risk: Write-capable tools can change calendars, chores, shared lists, meals, and related family hub data.

Mitigation: Review ambiguous or write-capable requests before allowing action, and treat dry-run responses as pending until the same call is re-issued with confirmation.

Risk: The described capabilities include media, messages, frame, member, and device data beyond the main discovery summary.

Mitigation: Review the installed MCP server's requested tools and account scope before deployment, especially in shared family environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)
- [npm package](https://www.npmjs.com/package/skylight-mcp)
- [Source repository](https://github.com/chrischall/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, configuration, API calls, guidance]

**Output Format:** [Markdown or text with JSON configuration examples and MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run responses for recurrence-scoped writes that require explicit confirmation before action.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
