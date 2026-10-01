## Description:

Build an operations task schedule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations staff use supplied scheduling guidance to prioritize tasks and select a start time for a local task schedule.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduling guidance can change task order and start time.

Mitigation: Review the proposed order and start time before acting on the schedule.

Risk: Execution creates local CSV schedule artifacts and may retain supplied request data.

Mitigation: Use a dedicated output directory and exclude unrelated sensitive data from the request JSON.

## Reference(s):

- [Operations Schedule Builder on ClawHub](https://clawhub.ai/wxt-ai/skills/task-priority-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON task schedule and local CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns ordered task IDs, the selected task ID and start time; writes a CSV schedule and reports a local receipt.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
