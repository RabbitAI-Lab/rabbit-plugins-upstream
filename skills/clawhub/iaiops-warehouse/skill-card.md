## Description:

Helps warehouse operations teams monitor industrial equipment, investigate downtime, and plan predictive maintenance across conveyor, sorting, and mobile-robot systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Warehouse operations and industrial automation teams use this skill to inspect equipment telemetry, analyze bottlenecks and downtime, and assess maintenance needs across conveyors, sorters, and AGV/AMR fleets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industrial control writes can change live equipment settings despite read-first positioning.

Mitigation: Require explicit authorization and change-management approval; enforce dry-run defaults and verify rollback before enabling production writes.

Risk: Publishing to production topics can affect connected warehouse systems.

Mitigation: Restrict publish permissions and verify that production topics require explicit authorization before installation.

## Reference(s):

- [iaiops-warehouse on ClawHub](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [Text, Analysis, Shell commands, Configuration guidance]

**Output Format:** [Text and Markdown with tool results and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational findings depend on site telemetry and configuration; some tools can write to control systems or publish messages.]

## Skill Version(s):

0.31.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
