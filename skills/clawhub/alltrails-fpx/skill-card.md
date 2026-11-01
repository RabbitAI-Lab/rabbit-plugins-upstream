## Description:

Use the fpx CLI with a signed-in AllTrails browser tab to search trails and read trail details, reviews, photos, weather, and personal hiking data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and hikers can use this skill to retrieve read-only AllTrails trail information and, with a signed-in browser session, their saved lists, completed trails, and activity feed from shell workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser pairing can make requested personal AllTrails data available to the agent.

Mitigation: Restrict approval to AllTrails and the declared header capture, request only needed personal data, and revoke pairing when it is no longer needed.

## Reference(s):

- [Endpoint examples](artifact/references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [AllTrails](https://www.alltrails.com)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; distances and elevation are returned in meters.]

## Skill Version(s):

3.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
