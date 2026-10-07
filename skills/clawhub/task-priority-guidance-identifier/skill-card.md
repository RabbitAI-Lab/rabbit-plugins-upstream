## Description:

Set service-class guidance for a task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to classify a task's service class and suggest its earliest start from a supplied task profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduling guidance may misclassify a task or overlook operational constraints.

Mitigation: Review the service class and earliest start against the full task context before scheduling.

Risk: The helper reads the supplied request JSON.

Mitigation: Provide only task information you are comfortable having the local script read.

## Reference(s):

- [Service Class Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/task-priority-guidance-identifier)

## Skill Output:

**Output Type(s):** [Guidance]

**Output Format:** [JSON containing a scheduling_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports a service class and earliest start without persisting an artifact.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
