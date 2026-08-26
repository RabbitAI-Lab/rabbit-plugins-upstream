## Description:

Clinical-facility edition of iaiops for hospital facilities monitoring and analysis across BACnet/IP BMS points, Modbus medical-gas and energy devices, OPC-UA plant SCADA, and clinical safety checks for isolation-room pressure and medical-gas source pressure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and facility engineers use this skill to inspect hospital BMS, medical-gas, SCADA, alarm, data-quality, and predictive-maintenance workflows with patient-safety framing. It is intended to support read-first clinical facilities checks such as isolation-room pressure, medical-gas source pressure, operating-room environment review, downtime triage, and compliance evidence preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports a mixed read/write clinical facilities skill with a high-impact BACnet write capability despite read-only positioning.

Mitigation: Treat BACnet writes as disabled unless dry-run defaults, named approvals, rollback or undo capture, and site authorization are enforced for hospital HVAC, pressure, or medical-gas control points.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, tool names, safety classifications, and structured check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first clinical facilities guidance; BACnet write actions are high-impact and require dry-run defaults, named approvals, rollback capture, and site authorization.]

## Skill Version(s):

0.23.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
