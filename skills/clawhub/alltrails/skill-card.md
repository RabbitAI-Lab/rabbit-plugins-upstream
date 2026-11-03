## Description:

This skill should be used when the user asks about AllTrails hiking/trail data. Triggers on phrases like "find trails near", "AllTrails", "trail details", "hike reviews", "trail conditions", "my saved trails", "trails I've completed", or any request involving hiking trails, trail search, reviews, photos, or a user's AllTrails lists and activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and their agents can search for trails, review trail details and conditions, and explore trail reviews, photos, and weather. With the user's signed-in AllTrails session, they can also inspect saved lists, completed trails, and activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in session can expose private hiking and profile data to the agent.

Mitigation: Use your own account, review which data the agent requests, and revoke pairing when finished.

Risk: The integration uses an unofficial AllTrails interface that may break or conflict with AllTrails' terms.

Mitigation: Review AllTrails' current terms before use and expect the integration to stop working if the service changes.

Risk: The browser bridge and npm package are external executable dependencies.

Mitigation: Review the extension's requested domains and capabilities, and consider pinning the npm package version.

## Reference(s):

- [alltrails-mcp package on npm](https://www.npmjs.com/package/alltrails-mcp)
- [Source repository linked by the skill documentation](https://github.com/chrischall/alltrails-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON data, GPX route data, Guidance]

**Output Format:** [Structured trail and account data, text summaries, and GPX 1.1 route documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; compact summaries are the default, with full records available when requested.]

## Skill Version(s):

3.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
