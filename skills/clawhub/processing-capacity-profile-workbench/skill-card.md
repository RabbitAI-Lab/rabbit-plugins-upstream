## Description:

Register a queued processing profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to register a selected processing profile as a queue record and receive its queue identifier, lane, and chunk count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send job results and a local artifact path to an arbitrary external endpoint without per-run consent.

Mitigation: Check CLAWHUB_DELIVERY_ENDPOINT and any --delivery-config before use; choose a controlled endpoint and avoid unintended ambient delivery settings.

## Reference(s):

- [Job Queue Register on ClawHub](https://clawhub.ai/wxt-ai/skills/processing-capacity-profile-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON object with a recorded profile and local effect receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local queue record; configured external delivery also returns a delivery receipt.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
