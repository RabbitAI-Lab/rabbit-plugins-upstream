## Description:

Provides service-class guidance and builds an operations task schedule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to assign service-class guidance to tasks and build a local task schedule from that guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream step writes a local schedule that may be unsuitable for real operations without review.

Mitigation: Use a dedicated output directory and review the generated schedule before relying on it.

## Reference(s):

- [Operations Scheduling Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/operations-scheduling-desk)

## Skill Output:

**Output Type(s):** [Guidance, Text, Files]

**Output Format:** [JSON response and local CSV schedule]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The upstream step returns scheduling guidance; the downstream step returns a task schedule and a receipt for its local CSV artifact.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
