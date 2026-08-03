## Description: <br>
Query AllTrails trail, review, photo, weather, saved-list, completed-trail, and activity-feed data through fpx CLI calls using the user's active browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect AllTrails data from shell workflows when an MCP server is unavailable or not desired. It guides read-only fpx requests for trail search and detail, reviews, photos, weather, route geometry, and signed-in user data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can surface personal AllTrails activity data through the user's signed-in browser session. <br>
Mitigation: Use account-specific endpoints only for data intentionally being inspected, and avoid storing or sharing user IDs, notes, completed trails, or activity-feed output unless necessary. <br>
Risk: Requests run through an active browser session and can fail or return misleading non-JSON responses when the session, extension bridge, or AllTrails app key is unavailable or stale. <br>
Mitigation: Confirm the Transporter bridge is connected, keep a signed-in AllTrails tab open when needed, check response bodies before use, and re-capture the app key when authorization errors occur. <br>
Risk: Extending beyond the documented read-only GET and read POST endpoints could affect account data. <br>
Mitigation: Keep usage limited to the documented read-only endpoints and review any added endpoint before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx) <br>
- [AllTrails endpoints for fpx](references/endpoints.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only AllTrails request guidance that depends on fpx, Transporter, and an active browser session for signed-in user data.] <br>

## Skill Version(s): <br>
2.1.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
