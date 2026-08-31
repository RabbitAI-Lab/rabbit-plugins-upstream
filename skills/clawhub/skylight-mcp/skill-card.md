## Description:

Read and manage a signed-in Skylight Calendar family hub, including calendar events, chores and rewards, shared lists, meal plans, frame members, devices, messages, and photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External Skylight account holders use this skill to let an agent inspect and update family calendars, chores, rewards, shopping and to-do lists, meal planning, frame or device data, members, and related media through a configured Skylight MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can provide broad read and write access to a shared Skylight family account, including calendars, chores, lists, meals, photos, messages, members, devices, rewards, and settings.

Mitigation: Install it only for accounts where that scope is acceptable, especially when the Skylight account is shared with family members.

Risk: The MCP configuration may contain Skylight account credentials.

Mitigation: Protect the MCP configuration like a password file and prefer a refresh token where supported.

Risk: Broad routing language can make vague requests more likely to trigger Skylight reads or writes.

Mitigation: Use explicit requests for account changes and treat dry-run responses for recurring event or chore writes as pending until reissued with confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/skylight-mcp)
- [npm package](https://www.npmjs.com/package/skylight-mcp)
- [Skylight Calendar](https://www.ourskylight.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool calls that read or modify Skylight account data after the user configures credentials.]

## Skill Version(s):

0.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
