## Description:

Read and manage a signed-in Skylight Calendar family hub, including calendar events, chores and reward stars, shared lists, meal plans, media, and frame settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP skill to let an agent inspect and update their own Skylight Calendar family hub. It supports household workflows such as reviewing calendars, managing chores, updating shared grocery or to-do lists, planning meals, and checking frame-related information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Skylight email and password credentials, giving the agent account-level access through the configured MCP server.

Mitigation: Use project-level MCP configuration instead of global configuration, protect the environment variables, and install only when this account access is acceptable.

Risk: The skill exposes broad read and write access to family calendar, chore, list, meal, media, and frame-related data.

Mitigation: Require explicit user confirmation before write or delete actions and review agent plans before allowing changes to shared household data.

Risk: Accounts with multiple Skylight frames may be affected beyond the intended frame if frame selection is left implicit.

Mitigation: Set SKYLIGHT_FRAME_ID where possible so operations are scoped to the intended family frame.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)
- [Artifact-declared source link](https://github.com/chrischall/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Skylight email and password environment variables; optional frame selection can scope operations when multiple frames are available.]

## Skill Version(s):

0.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
