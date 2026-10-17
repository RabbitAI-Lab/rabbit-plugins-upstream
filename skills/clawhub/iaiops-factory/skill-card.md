## Description:

Helps factory engineers inspect industrial devices and production data across multiple protocols, diagnose downtime, calculate OEE, and perform explicitly approved control changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Factory engineers and operations teams use this skill to inspect PLCs, CNC equipment, sensors, and production-line telemetry, troubleshoot data flow and downtime, and prepare OEE and asset reports. Production control changes require separate authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PLC writes, MQTT publishing, EtherCAT state changes, and PROFINET address changes can disrupt production equipment or networks.

Mitigation: Keep live writes disabled until authorized; require named approval, dry-run review, a rollback plan, and isolated factory-network access.

Risk: Factory credentials or network access could expose operational systems.

Mitigation: Use managed credential storage and verify network isolation before connecting to live equipment.

## Reference(s):

- [iaiops-factory on ClawHub](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration drafts]

**Output Format:** [Structured diagnostic results and human-readable reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first; live control operations require change approval and default to dry run.]

## Skill Version(s):

0.29.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
