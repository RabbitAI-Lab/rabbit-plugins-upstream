## Description:

Provides read-only AllTrails hiking and trail data, including trail search, trail details, reviews, photos, weather, GPX route export, and signed-in account lists or activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer questions about hiking trails, trail conditions, reviews, photos, weather, GPX routes, and their own AllTrails saved or completed trail data through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read personal AllTrails profile, saved-list, completed-trail, and activity-feed data when those tools are invoked.

Mitigation: Use the skill only with accounts and sessions you intend to expose, and avoid personal-data tools unless the request requires them.

Risk: The skill depends on an unofficial AllTrails integration through a signed-in browser session and may fail if the site, session, or bridge state changes.

Mitigation: Keep the browser bridge paired only when needed, confirm the AllTrails tab is signed in, and use the healthcheck tool when requests fail.

Risk: AllTrails data access is read-only but may still be governed by AllTrails terms and site controls.

Mitigation: Use the skill at the user's discretion for their own account and review proposed uses before relying on automated access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails)
- [npm package: alltrails-mcp](https://www.npmjs.com/package/alltrails-mcp)
- [Source repository: alltrails-mcp](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration examples and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or full AllTrails records, GPX route content, reviews, photos, weather summaries, and diagnostics depending on the invoked tool.]

## Skill Version(s):

3.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
