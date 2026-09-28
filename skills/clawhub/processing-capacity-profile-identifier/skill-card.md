## Description:

Selects a processing profile for a supplied workload and deadline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and developers use this skill to choose a processing profile for a batch workload from its record count and deadline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A selected profile may not reflect real-world capacity or scheduling constraints.

Mitigation: Review the profile against actual capacity and deadline requirements before scheduling work.

## Reference(s):

- [Processing Capacity Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/processing-capacity-profile-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object with a processing_profile string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The profile is one of latency-first, batch-balanced, or throughput-first; no business artifact is persisted.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
