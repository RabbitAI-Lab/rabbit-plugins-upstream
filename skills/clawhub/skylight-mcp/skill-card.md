## Description:

Read and manage Skylight Calendar family hub data, including calendar events, chores and rewards, shared lists, meal plans, messages, photos, device settings, and member access using a signed-in Skylight account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and household administrators use this skill to let an agent inspect and update their Skylight family hub, including calendars, chores, rewards, lists, meals, photos, messages, devices, and member access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server requires a Skylight email and password and can access household calendar, list, meal, photo, message, device, member, invitation, approval, and visibility data.

Mitigation: Use a project-local MCP configuration, limit account privileges where possible, consider a dedicated Skylight account, and install only when this level of account access is acceptable.

Risk: Agent-initiated writes can change household content or access settings, including invitations, approvals, and public visibility when confirmed.

Mitigation: Review tool arguments and dry-run previews before confirmation, especially for recurrence-scoped writes and access or visibility changes.

Risk: Running the documented npx command installs and executes the package from npm at setup time.

Mitigation: Review npm and source provenance before use and prefer pinned, reviewed versions in controlled environments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [Text, JSON, API Calls, Configuration instructions]

**Output Format:** [MCP tool responses with structured JSON or text summaries, plus JSON configuration snippets for setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Skylight email and password environment variables; some broad write or access-changing actions return dry-run previews until explicitly confirmed.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
