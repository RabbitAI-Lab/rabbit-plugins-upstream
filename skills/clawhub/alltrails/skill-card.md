## Description:

Provides read-only AllTrails trail search, trail details, reviews, photos, weather, GPX export, and signed-in user list and activity access through an unofficial MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find trails, inspect trail details, reviews, weather, photos, and GPX data, and review signed-in AllTrails saved lists, completed trails, or activity when intentionally connected to their AllTrails session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned npm package through npx while connected to a signed-in browser session.

Mitigation: Pin alltrails-mcp to a trusted version, use a restricted browser profile or account, and enable it only when intentionally retrieving AllTrails data.

Risk: The AllTrails integration is unofficial, reverse-engineered, and may break or conflict with AllTrails terms or bot-protection controls.

Mitigation: Review the applicable terms before use, expect service changes, and avoid relying on it for critical route safety decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source link from skill documentation](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON configuration and tool-call summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only trail and account data summaries; GPX output may be returned for trail route export.]

## Skill Version(s):

2.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
