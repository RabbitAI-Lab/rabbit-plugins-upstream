## Description:

Helps industrial teams inspect and troubleshoot discrete-manufacturing equipment across PLC, CNC, sensor, and messaging protocols, with approval-gated control writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial operators and engineers use this skill to inspect production-line devices, diagnose downtime and data quality, and analyze OEE and assets. Control-system changes require an authorized maintenance approval process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PLC writes, network readdressing, and motion-state changes can disrupt industrial operations.

Mitigation: Keep write tools disabled unless authorized maintenance staff complete the documented MOC approval and dry-run checks.

Risk: Raw-socket protocols and production credentials expose sensitive operational systems.

Mitigation: Restrict raw-socket access and production credentials to authorized, isolated maintenance environments.

Risk: Chinese-only operating instructions may be misunderstood by reviewers.

Mitigation: Have a qualified reviewer read the instructions carefully before enabling the skill.

## Reference(s):

- [iaiops-factory on ClawHub](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown guidance and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first workflows; control writes are described as approval-gated and dry-run by default.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
