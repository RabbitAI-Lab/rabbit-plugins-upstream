## Description:

Query AllTrails trail search, trail details, reviews, photos, weather, and signed-in user data from a shell with fpx through a signed-in browser tab instead of running alltrails-mcp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve read-only AllTrails data from shell workflows without installing or running the MCP server. It is especially relevant when personal lists, completed trails, or activity feeds require the user's active signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query saved lists, completed trails, activity feeds, and profile data through the user's active AllTrails browser session.

Mitigation: Run it only when the signed-in user explicitly wants that data retrieved, avoid unattended use against personal endpoints, and treat exported activity or profile data as private.

## Reference(s):

- [AllTrails endpoints for fpx](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only fpx requests through an active browser session; personal AllTrails activity and profile data should be handled as private.]

## Skill Version(s):

2.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
