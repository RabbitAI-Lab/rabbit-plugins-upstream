## Description:

Read and manage a signed-in Skylight Calendar family hub, including calendar events, chores and reward stars, shared lists, meal plans, messages, media uploads, and frame or member settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Skylight Calendar users use this skill to let an agent query and update family-hub data such as events, chores, lists, meals, photos, messages, and frame or member settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for Skylight account credentials and can use them to access family-hub data.

Mitigation: Prefer project-local configuration or a scoped and revocable refresh token if available, and avoid storing reusable passwords in global configuration.

Risk: The skill exposes broader read and write access than the manifest and tool list clearly surface.

Mitigation: Enable it only where broad Skylight account access is acceptable and review agent requests before allowing writes.

Risk: Running the MCP server through an unpinned npm invocation can install a newer package version later.

Mitigation: Pin the npm package version when the host environment supports pinned MCP server commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON configuration examples and Skylight MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent actions can read or modify Skylight account data after credentials are configured.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
