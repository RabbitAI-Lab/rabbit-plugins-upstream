## Description:

Helps agents find trails, reviews, photos, and weather on AllTrails and access a signed-in user's saved trails and activity through an unofficial read-only integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and agents helping them can search trails, review trail details and conditions, and retrieve saved lists or completed hikes when the user has a signed-in AllTrails session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial integration uses a signed-in browser tab and bridge to access personal hiking data.

Mitigation: Use project-scoped configuration, inspect the npm package and bridge before installing, and remove the server and extension when no longer needed.

Risk: Generic hiking requests may activate access to AllTrails data unexpectedly.

Mitigation: Confirm the user's intent before retrieving account-backed lists or activity.

## Reference(s):

- [AllTrails skill listing](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, GPX files, Configuration guidance]

**Output Format:** [Markdown guidance, structured trail data, or GPX 1.1 route export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only trail and account-backed data; compact responses by default, with full records available on request.]

## Skill Version(s):

3.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
