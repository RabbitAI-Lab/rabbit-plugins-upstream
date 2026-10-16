## Description:

Provides read-only AllTrails trail discovery, details, reviews, photos, weather, and signed-in account information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and agents can find trails and review routes, conditions, and community feedback. With explicit permission, they can also consult a signed-in user's saved lists, completed trails, and activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in browser session can expose private profile, lists, completed trails, and activity data.

Mitigation: Prefer public trail search and access personal account tools only with the user's explicit permission.

Risk: The unofficial integration depends on an internal AllTrails API and a signed-in browser bridge; automated use may conflict with AllTrails terms or stop working.

Mitigation: Review AllTrails terms and confirm the user accepts this integration before installing; do not rely on it for critical trail decisions.

## Reference(s):

- [ClawHub alltrails skill](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, GPX route data]

**Output Format:** [Structured trail or account records and optional GPX 1.1 export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact records by default; full records available on request.]

## Skill Version(s):

3.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
