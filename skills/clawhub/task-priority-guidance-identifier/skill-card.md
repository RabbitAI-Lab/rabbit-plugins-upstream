## Description:

Set service-class guidance for a task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and scheduling agents use this skill to turn a task profile with urgency, due date, and staffing details into concise service-class scheduling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incomplete urgency, due date, or staffing details can produce misleading service-class guidance.

Mitigation: Confirm the task_profile contains the needed scheduling facts before relying on the recommendation.

Risk: Task details may include unnecessary sensitive operational context.

Mitigation: Provide only the task details needed for the current scheduling request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/task-priority-guidance-identifier)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [String returned in the scheduling_guidance output field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise scheduling guidance based only on the task_profile supplied in the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
