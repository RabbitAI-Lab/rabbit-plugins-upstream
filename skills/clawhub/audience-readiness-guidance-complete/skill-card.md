## Description:

Classifies stakeholder briefs by audience, prepares client-facing section previews with recorded omissions, and optionally delivers results to a configured endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and communications teams use the skill to classify a stakeholder brief, identify sections suitable for clients, and save a local preview. They can also deliver the result to an explicitly configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive the brief result and local artifact path without per-run confirmation.

Mitigation: Clear unrelated delivery and SMTP environment variables before running; use only a trusted, intended destination.

Risk: Local brief outlines are written to the chosen output directory.

Mitigation: Choose an appropriate output directory and review its contents before sharing.

## Reference(s):

- [Audience Readiness Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/audience-readiness-guidance-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local briefing preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes audience, included and excluded sections, a local artifact receipt, and a delivery status receipt.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
