## Description:

Read and manage a signed-in user's Skylight Calendar family hub, including calendar events, chores and rewards, shared lists, meal plans, media, and frame settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their own Skylight account so it can inspect and update family calendar, chores, rewards, shopping and to-do lists, meal plans, media, and frame-related settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned third-party MCP package with reusable Skylight account credentials.

Mitigation: Use a dedicated Skylight account where possible, avoid committing or sharing MCP configuration files that contain credentials, restrict local config file permissions, and prefer a pinned, reviewed package version or a locally installed trusted executable.

Risk: The connector can access and modify private family-hub data, including media and settings.

Mitigation: Review requested tool actions before execution, especially writes, uploads, deletions, or changes that affect shared family calendars, chores, lists, meals, media, frames, devices, or members.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [Skylight website](https://www.ourskylight.com)
- [npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with JSON and inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to call Skylight MCP tools that read or modify private family-hub data.]

## Skill Version(s):

0.10.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
