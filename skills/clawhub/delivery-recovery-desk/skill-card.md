## Description:

Advise bounded retry policies and record recovery schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations employees use this skill to select a retry mode for recovery requests and convert failed delivery handoffs into bounded retry schedules and next-action records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated retry schedules could be applied incorrectly to real customer or business workflows.

Mitigation: Review generated retry schedules before applying them, especially when the request is broader than the two documented recovery stages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/delivery-recovery-desk)

## Skill Output:

**Output Type(s):** [guidance, configuration]

**Output Format:** [String or object with retry schedule fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include retry_mode or recorded_retry_mode with attempts remaining, ordered retry times, and next action when scheduling is possible.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
