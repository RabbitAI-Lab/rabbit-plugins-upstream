## Description:

This skill helps an agent use a Kia Access MCP server to read vehicle status, location, EV charge state, and perform confirm-gated door, climate, and charging commands through the user's Kia Owners account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their own Kia Access account for vehicle status checks, EV charging information, location lookup, and explicitly confirmed remote vehicle commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access Kia account data, locally persisted sessions, vehicle status, and vehicle location.

Mitigation: Install only when that access is acceptable, protect Kia credentials and refresh tokens, and avoid sharing session material in conversations or logs.

Risk: Remote commands can affect a real vehicle, including unlocking doors, climate control, and charging behavior.

Mitigation: Use KIA_WRITE_MODE=none for read-only access unless commands are needed, and require explicit user confirmation before any vehicle command.

Risk: A command accepted by Kia may not mean the vehicle actually changed state, and cached reads can be stale.

Mitigation: Report accepted commands separately from confirmed state, refresh or re-read vehicle status when freshness matters, and avoid describing dry runs as completed actions.

## Reference(s):

- [npm package: kiaaccess-mcp](https://www.npmjs.com/package/kiaaccess-mcp)
- [Source repository listed by skill](https://github.com/chrischall/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, API calls]

**Output Format:** [Markdown with JSON configuration examples and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews and requires explicit user confirmation before vehicle commands.]

## Skill Version(s):

0.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
