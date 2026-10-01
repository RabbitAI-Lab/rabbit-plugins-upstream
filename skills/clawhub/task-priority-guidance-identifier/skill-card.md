## Description:

Set service-class guidance for a task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations planners and task coordinators use a supplied task profile to determine a service class and earliest-start guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Service-class guidance may not reflect all due-date or staffing constraints.

Mitigation: Confirm the proposed class and start time against the full task profile before scheduling.

Risk: Generic documentation refers to output directories and effect receipts that this operation does not use.

Mitigation: Use the default local invocation and its returned guidance; review changes before enabling downstream behavior.

## Reference(s):

- [Service Class Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/task-priority-guidance-identifier)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON object containing a scheduling_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Computed locally without persisting a business artifact.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
