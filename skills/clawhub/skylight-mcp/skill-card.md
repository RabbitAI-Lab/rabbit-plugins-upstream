## Description:

Connects an agent to a signed-in Skylight Calendar family hub to read and manage calendar events, chores, rewards, shared lists, meals, frames, devices, messages, media, and settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate against their own Skylight family hub for household scheduling, chores, shared lists, meal planning, media, and frame management. It is suited to users who are comfortable granting an MCP server access to sensitive family account data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires persistent Skylight account credentials and can access household schedules, chores, lists, meals, media, messages, and settings.

Mitigation: Use project-scoped MCP configuration when possible, protect the stored password, and install only for accounts where this level of access is acceptable.

Risk: The server can perform create, update, delete, upload, and settings actions against the connected family hub.

Mitigation: Review agent-proposed write, upload, delete, and settings operations before allowing them to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight](https://www.ourskylight.com)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON configuration and tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP configuration snippets that store Skylight email and password environment variables.]

## Skill Version(s):

0.7.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
