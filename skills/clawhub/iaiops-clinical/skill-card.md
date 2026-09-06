## Description:

Clinical-facility edition of iaiops for hospital facilities teams, combining BACnet/IP, Modbus, OPC-UA, and cross-protocol analysis for isolation-room pressure, medical-gas, operating-room environment, downtime, alarms, and compliance-oriented facility workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External healthcare facilities, clinical engineering, and operations teams use this skill to inspect hospital BMS, medical-gas, SCADA, alarm, and downtime evidence across BACnet/IP, Modbus, and OPC-UA. It supports patient-safety-oriented triage and reporting while leaving site safety systems, alarms, and authorized change controls as the source of truth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents the edition as read-only while also documenting a real BACnet write function.

Mitigation: Deploy only where BACnet write access is technically disabled or separately authorized, controlled, and reviewed through change management.

Risk: Clinical facility checks can affect patient-safety workflows if treated as authoritative control decisions.

Mitigation: Use the skill as decision support; rely on site alarms, infection-control procedures, medical-gas systems, and authorized clinical engineering review for final action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical)
- [Publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured operational guidance with inline commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include protocol-specific checks, ranked findings, cited readings, workflow steps, and change-control guidance.]

## Skill Version(s):

0.27.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
