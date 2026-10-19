## Description:

Helps facilities teams inspect building automation data across BACnet, Modbus, IO-Link, MQTT, and supervisory controllers, analyze HVAC and meter behavior, and request approval-gated control changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Facilities operators and building automation engineers use this skill to discover and read equipment points, investigate HVAC faults and electricity use, and prepare authorized control changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device writes can alter HVAC setpoints or equipment operation.

Mitigation: Use only in authorized facilities; keep dry run enabled until change approval is complete and verify target points before execution.

Risk: Control changes could affect life-safety systems or production equipment.

Mitigation: Do not use write tools on life-safety systems or production equipment without site authorization.

## Reference(s):

- [iaiops-building ClawHub release](https://clawhub.ai/zw008/skills/iaiops-building)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device changes require named approval and default to dry run.]

## Skill Version(s):

0.31.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
