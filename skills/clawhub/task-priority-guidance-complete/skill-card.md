## Description:

Assigns service-class guidance from a task profile, builds an operations schedule, saves it locally, and optionally submits it to a configured delivery endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations planners and developers use this skill to turn a task profile into service-class guidance and a saved task schedule, with optional live delivery when configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured live delivery can submit schedule data and the local artifact path to an arbitrary endpoint without a separate confirmation step.

Mitigation: Keep delivery endpoint and API key settings unset unless live submission is intended; review the destination and schedule before enabling it.

Risk: The skill creates local schedule artifacts during a run.

Mitigation: Use a dedicated output directory and review the saved schedule before sharing it.

## Reference(s):

- [Service Class Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/task-priority-guidance-complete)

## Skill Output:

**Output Type(s):** [JSON, CSV file]

**Output Format:** [JSON result and locally saved CSV task schedule]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local artifact receipt and a delivery status receipt; live submission is optional.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
