## Description:

This skill helps agents use an unofficial AllTrails MCP server to search trails, inspect trail details, reviews, photos, weather, and GPX routes, and read signed-in user AllTrails lists and activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to retrieve AllTrails trail information, reviews, photos, route exports, weather, saved lists, completed trails, or activity data through a signed-in AllTrails browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can execute an unpinned third-party MCP package.

Mitigation: Pin alltrails-mcp to a specific reviewed version instead of relying on automatic latest-version execution.

Risk: The MCP server operates through a signed-in AllTrails browser session and may access private profile, saved-list, completed-trail, and activity data.

Mitigation: Run it only with the minimum browser/session access needed for the intended AllTrails task, and avoid using accounts or sessions that contain data outside that scope.

Risk: The skill depends on a reverse-engineered AllTrails API and browser bridge behavior that may break or conflict with AllTrails terms.

Mitigation: Review AllTrails terms and operational constraints before use, and re-check behavior after AllTrails site or API changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/alltrails)
- [npm package: alltrails-mcp](https://www.npmjs.com/package/alltrails-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool outputs may include compact or full AllTrails records, GPX route data, trail photos, reviews, weather, saved-list entries, completed trails, and activity feed items.]

## Skill Version(s):

2.3.3 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
