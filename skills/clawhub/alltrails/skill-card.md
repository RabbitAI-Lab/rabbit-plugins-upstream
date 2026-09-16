## Description:

This skill should be used when the user asks about AllTrails hiking/trail data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search AllTrails hiking data, inspect trail details, reviews, photos, weather, GPX routes, and signed-in user trail lists or activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration is unofficial, depends on AllTrails internal behavior, and may violate AllTrails terms or stop working.

Mitigation: Install only when that risk is acceptable, keep the skill scoped to explicit AllTrails requests, and review terms before operational use.

Risk: Setup runs external code through npx and depends on a browser extension.

Mitigation: Pin and audit the alltrails-mcp package and the browser extension before use.

Risk: The skill operates through a signed-in AllTrails browser session.

Mitigation: Use a dedicated or low-sensitivity AllTrails account where possible and avoid enabling the skill for unrelated hiking questions.

## Reference(s):

- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source link from skill documentation](https://github.com/chrischall/alltrails-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with inline JSON configuration and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or full AllTrails records, GPX route data, trail reviews, photos, weather, saved lists, completed trails, and activity feed summaries.]

## Skill Version(s):

2.3.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
