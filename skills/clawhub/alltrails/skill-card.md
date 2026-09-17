## Description:

This skill helps agents answer requests about AllTrails hiking and trail data, including trail search, details, reviews, photos, weather, saved lists, completed trails, and activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to let an agent retrieve read-only AllTrails trail, review, photo, weather, saved-list, completed-trail, and activity-feed information for hiking workflows. It is most useful when the user has an AllTrails browser session available and wants agent assistance finding or reviewing trail data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local MCP package and release evidence notes that the package may be unpinned.

Mitigation: Prefer project-local MCP configuration, pin the npm package to a reviewed version, and inspect the package or source before enabling it.

Risk: The skill can access signed-in AllTrails profile, saved-list, completed-trail, and activity-feed data through the user's browser session.

Mitigation: Require user confirmation before using account-specific tools and install the skill only when read access to the signed-in AllTrails session is acceptable.

Risk: The skill depends on AllTrails behavior that may change or be restricted.

Mitigation: Use the healthcheck when calls fail, expect service-side changes to break workflows, and review AllTrails terms before automated use.

## Reference(s):

- [ClawHub alltrails skill page](https://clawhub.ai/chrischall/skills/alltrails)
- [npm package alltrails-mcp](https://www.npmjs.com/package/alltrails-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only AllTrails-oriented guidance and tool-use instructions; several tools support compact and full response views.]

## Skill Version(s):

2.3.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
