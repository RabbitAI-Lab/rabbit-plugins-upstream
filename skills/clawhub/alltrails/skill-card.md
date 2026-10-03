## Description:

Helps users search AllTrails for hikes and review trail details, conditions, photos, and their own hiking activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and other users can discover trails, review route information and conditions, and, when authorized, inspect their saved trails and activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trail-related triggers could expose personal AllTrails data from a signed-in session without a clear request.

Mitigation: Invoke account-scoped tools only when the user explicitly requests saved trails, completed trails, profile, or activity.

Risk: The unofficial integration uses an external npm package and a bridge to a signed-in browser tab.

Mitigation: Review the package and browser bridge before installation, and use them only for explicit AllTrails tasks.

## Reference(s):

- [AllTrails MCP npm package](https://www.npmjs.com/package/alltrails-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, GPX route data]

**Output Format:** [Markdown or GPX 1.1 XML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trail and account results may include reviews, photos, weather, saved lists, and activity.]

## Skill Version(s):

3.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
