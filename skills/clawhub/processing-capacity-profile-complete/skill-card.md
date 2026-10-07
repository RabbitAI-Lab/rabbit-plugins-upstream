## Description:

Selects a processing profile from a workload, records the resulting queue entry locally, and optionally submits it to a configured delivery target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to select a processing profile for a workload and record a queued job, with optional delivery to a configured endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery settings can submit queue records externally without a separate confirmation step.

Mitigation: Before running, review delivery endpoints, API keys, and delivery configuration; leave delivery settings unset for local-only operation.

## Reference(s):

- [Processing Capacity Planner release](https://clawhub.ai/wxt-ai/skills/processing-capacity-profile-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local queue record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the chosen profile, recorded queue entry, local artifact receipt, and delivery outcome.]

## Skill Version(s):

1.2.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
