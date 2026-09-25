## Description:

Query alltrails.com for trail search, trail details, reviews, photos, weather, and signed-in account data from a shell through fpx and a user's own browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill to retrieve AllTrails trail data and selected signed-in account data from shell workflows without running an MCP server. It is suited for read-only lookups, scripting, and troubleshooting when a paired browser tab and fpx are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in AllTrails browser session to read personal account information such as saved lists, completed trails, and activity feed data.

Mitigation: Use public trail commands for ordinary lookups, and run account-specific commands only when you intentionally want that signed-in account data exposed to the agent or shell output.

Risk: The fpx workflow depends on a paired Transporter browser extension and an open AllTrails tab, so command output may fail or reflect browser-session state rather than a standalone API credential.

Mitigation: Confirm the browser tab is open, signed in when needed, and paired before relying on command output; re-capture the AllTrails app key when requests return missing-key or stale-key errors.

## Reference(s):

- [AllTrails endpoints for fpx](references/endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with shell command examples and JSON response-shape guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails calls through fpx; user/account endpoints require a signed-in browser tab and may expose account data in command output.]

## Skill Version(s):

3.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
