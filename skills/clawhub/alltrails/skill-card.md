## Description:

Helps users find hiking trails and review trail details, weather, and their own AllTrails lists and activity through an unofficial read-only integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and trip planners use this skill to search trails, read trail details and reviews, and inspect their own saved trails and hiking history with a signed-in AllTrails session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in browser session can expose your AllTrails profile, saved lists, completed trails, and activity to the integration.

Mitigation: Invoke it only for explicit AllTrails requests, and review the npm package and browser extension before installing them.

Risk: This unofficial integration relies on an internal AllTrails API that may change; automated use may conflict with AllTrails terms.

Mitigation: Use it with your own account at your discretion and confirm important trail information directly with AllTrails.

## Reference(s):

- [AllTrails skill on ClawHub](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Structured trail data, GPX route data]

**Output Format:** [Markdown or structured data; GPX 1.1 for route exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails lookups; personal results require a signed-in browser session.]

## Skill Version(s):

3.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
