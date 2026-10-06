## Description:

Build a client-facing brief from approved sections while recording omissions for internal follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Communications teams use this skill to select audience-approved sections for a client brief and track omitted sections for internal follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured external delivery can send generated briefing data and a local file path to an endpoint.

Mitigation: Use a dedicated output directory; review delivery settings before installation and enable endpoint delivery only after approving its destination and payload.

## Reference(s):

- [Client Brief Composer on ClawHub](https://clawhub.ai/wxt-ai/skills/audience-readiness-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON briefing preview and a local brief artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes audience, included and excluded section identifiers, and a local artifact receipt; configured delivery also returns a delivery receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
