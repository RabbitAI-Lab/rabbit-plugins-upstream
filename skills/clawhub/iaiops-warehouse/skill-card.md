## Description:

Helps warehouse operations teams analyze conveyor, sorter, and mobile-robot telemetry for maintenance, downtime, throughput, and alarm investigations across industrial protocols.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Warehouse operations engineers and maintenance teams use the skill to investigate material-handling equipment, diagnose downtime and bottlenecks, and plan predictive maintenance using industrial telemetry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite its read-only description, the skill documents controls that can change production equipment settings.

Mitigation: Require explicit operator approval for write tools and enforce dry runs in the runtime; do not rely on the read-only description for access policy.

Risk: Publishing and export tools can send operational messages or write files.

Mitigation: Gate publishing and file-writing tools under operator approval and limit them to approved destinations.

## Reference(s):

- [iaiops-warehouse ClawHub release](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration instructions]

**Output Format:** [Text and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational diagnostics, forecasts, and configuration drafts.]

## Skill Version(s):

0.32.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
