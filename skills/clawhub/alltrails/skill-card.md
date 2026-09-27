## Description:

Provides read-only AllTrails trail discovery, details, reviews, weather, and access to a signed-in user's saved lists and hiking history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and other AllTrails users can ask an agent to find trails, review trail information, and explore their own saved lists and completed hikes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial integration uses internal AllTrails APIs and may violate AllTrails terms or stop working.

Mitigation: Review the terms and accept the integration's limitations before installing or relying on it.

Risk: The browser bridge uses a signed-in AllTrails tab and a fetchproxy extension to access account data.

Mitigation: Request only trail or account data you intend to access, and review the npm package and source before trusting it.

## Reference(s):

- [AllTrails skill on ClawHub](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source code (linked by skill)](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, GPX]

**Output Format:** [Text responses, structured trail data, and GPX 1.1 route exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; compact records by default, with full records on request.]

## Skill Version(s):

3.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
