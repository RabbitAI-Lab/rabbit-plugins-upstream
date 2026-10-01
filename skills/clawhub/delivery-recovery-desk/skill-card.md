## Description:

Set delivery recovery guidance and turn delivery failures into bounded retry schedules and next-action handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations teams use this skill to select recovery guidance after a failed delivery, schedule remaining retries within the selected policy, and record the next handoff action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated retry schedule could be mistaken for approved operational guidance.

Mitigation: Review the schedule against the active delivery policy before using it.

Risk: The downstream operation creates a CSV retry schedule in the chosen local output directory.

Mitigation: Use a dedicated, writable output directory and review its generated files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/delivery-recovery-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON recovery guidance and retry handoff; CSV retry schedule for downstream use]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream writes a local retry-schedule artifact to a caller-selected output directory.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
