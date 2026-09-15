## Description:

Query alltrails.com trail, review, photo, weather, saved-list, completed-trail, and activity-feed data from a shell through the fpx CLI and a user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query AllTrails data from scripts or shell workflows when the AllTrails MCP server is unavailable or not desired. It is suited for read-only trail discovery, trail detail lookup, reviews, photos, weather, saved lists, completed trails, and account-linked activity feed queries authorized by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose account-linked AllTrails data and captured request headers from a signed-in browser session.

Mitigation: Use it only with accounts and profile data you are authorized to access, avoid sharing captured headers or temporary capture files, and keep generated outputs scoped to the requested query.

Risk: Installing and pairing fpx/Transporter gives shell commands access to data visible to the paired AllTrails tab.

Mitigation: Review or pin @fetchproxy/cli before installation, avoid sudo for npm installation, and pair only with a browser session whose visible data is appropriate for the task.

## Reference(s):

- [AllTrails endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails request guidance using fpx, Transporter, captured headers, and JSON response inspection.]

## Skill Version(s):

2.3.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
