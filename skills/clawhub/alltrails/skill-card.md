## Description:

This skill should be used when the user asks about AllTrails hiking/trail data. Triggers on phrases like "find trails near", "AllTrails", "trail details", "hike reviews", "trail conditions", "my saved trails", "trails I've completed", or any request involving hiking trails, trail search, reviews, photos, or a user's AllTrails lists and activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve read-only AllTrails trail search results, trail details, reviews, photos, weather, saved lists, completed trails, and activity data through the alltrails-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an unofficial reverse-engineered AllTrails integration that may break or conflict with AllTrails terms.

Mitigation: Use it only when you accept the third-party integration risk, and remove the MCP entry if you no longer need AllTrails access.

Risk: The MCP server depends on a signed-in browser tab and can expose account-scoped AllTrails data to the agent.

Mitigation: Prefer project-level MCP configuration, keep the browser bridge disabled when not in use, and close or sign out of the AllTrails tab when access is not needed.

Risk: The trigger scope is broader than necessary for hiking and trail prompts.

Mitigation: Review activation behavior before deployment and keep the skill enabled only in workspaces where AllTrails access is expected.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration examples and tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only AllTrails MCP setup guidance, workflow steps, and compact or full trail data responses depending on tool view settings.]

## Skill Version(s):

3.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
