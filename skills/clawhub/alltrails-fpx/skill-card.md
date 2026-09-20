## Description:

Query AllTrails trail, review, photo, weather, saved-list, completed-trail, and activity-feed data from a shell through fpx using a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to issue read-only AllTrails lookups and account-scoped queries from shell workflows when the AllTrails MCP server is unavailable or not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands run through fpx in a signed-in browser context can access account-scoped AllTrails data such as saved lists, completed trails, profile, and activity feed.

Mitigation: Use only with intended AllTrails sessions, treat captured outputs as private account data, and remove the fpx profile or browser pairing when access is no longer needed.

Risk: Captured app headers can become stale or fail when the browser tab has not cleared AllTrails access checks.

Mitigation: Recapture headers from active tab traffic and confirm the signed-in browser tab is available before retrying commands.

## Reference(s):

- [AllTrails fpx endpoint examples](references/endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only examples; account-scoped commands may expose private AllTrails profile data.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
