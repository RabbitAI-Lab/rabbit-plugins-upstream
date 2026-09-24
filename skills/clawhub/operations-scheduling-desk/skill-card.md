## Description:

Derive service classes and build operations task schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and scheduling agents use this skill to classify operational tasks by service class and produce concise task schedules from user-provided urgency, due date, staffing, and scheduling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduling guidance or task schedules may be incorrect if the user supplies incomplete urgency, due date, staffing, or prior guidance details.

Mitigation: Review the proposed guidance and schedule against the current operations context before using it.

Risk: The skill only needs current-request scheduling details and does not require private files or credentials.

Mitigation: Provide only the task information needed for scheduling, and avoid adding sensitive credentials or unrelated private data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/operations-scheduling-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [guidance, configuration, text]

**Output Format:** [Text and structured object fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces scheduling_guidance as a string and task_schedule as an object with ordered_task_ids, scheduled_task_id, and scheduled_start.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
