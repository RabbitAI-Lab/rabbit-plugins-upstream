## Description:

Query alltrails.com trail, review, photo, weather, saved-list, completed-trail, and activity-feed data from a shell through the fpx CLI and a browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare shell commands for read-only AllTrails lookups when they need trail or account data through an authenticated browser session instead of an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes AllTrails API reads through a browser session, so signed-in account context may be used for personal lists, completed trails, and activity-feed requests.

Mitigation: Use a signed-out tab for public trail lookups where possible, and run signed-in requests only when account-specific data is needed.

Risk: The workflow depends on fpx and the Transporter extension making read-only requests from the user's browser session.

Mitigation: Install only when that access model is acceptable, limit browser extension site access to AllTrails, and review or pin @fetchproxy/cli before global installation.

## Reference(s):

- [AllTrails endpoint examples](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails request guidance that depends on fpx, the Transporter browser extension, and a browser session for signed-in data.]

## Skill Version(s):

2.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
