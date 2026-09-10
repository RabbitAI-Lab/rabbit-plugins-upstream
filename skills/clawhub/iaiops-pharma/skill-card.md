## Description:

Iaiops Pharma helps agents work with pharmaceutical manufacturing OT contexts across BACnet/IP, Modbus, HART-IP, and OPC-UA, with checks for cleanroom pressure cascades, particle counts, pharmaceutical water, alarms, data quality, readiness, and change-control evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, plant engineers, and validation teams use this skill to guide agents through pharma OT monitoring and analysis workflows for GMP plants, including cleanroom, water-system, alarm, asset, data-quality, investigation, and PLC change-control tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises a read-only pharma edition while server security evidence says it exposes a high-impact BACnet write operation for live building or cleanroom systems.

Mitigation: Review before installation in real facilities; enable only where BACnet writes are blocked, separately approved, or intentionally available under formal change control.

Risk: Pharmaceutical checks rely on facility-provided quality limits, temperature assumptions, and declared cleanroom adjacency, so incomplete site inputs can make results incomplete or not gradable.

Mitigation: Require facility-approved particle, conductivity, TOC, temperature, and cleanroom door/topology inputs before using outputs to support GxP decisions.

Risk: Some protocol coverage is marked as unverified or out of scope, including PI historian connectivity, live BACnet HVAC/COV/write paths, HART gateway testing, S7 real-device validation, GxP crosswalks, and LIMS/QMS/MES integration.

Mitigation: Confirm site-specific protocol support and validation status before deployment, and keep unsupported enterprise quality systems outside this skill's operational scope.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline tool names, commands, configuration values, and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed before facility use, especially where BACnet writes or GxP decisions are involved.]

## Skill Version(s):

0.27.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
