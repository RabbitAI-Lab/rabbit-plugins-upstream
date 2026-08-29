## Description:

iaiops-clinical helps agents inspect hospital facility systems across BACnet/IP, Modbus, and OPC-UA, with patient-safety checks for isolation-room pressure, medical gas, operating-room environment, alarms, and cross-protocol diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical facilities teams, healthcare integrators, and operations engineers use this skill to investigate hospital BMS, medical-gas, SCADA, alarm, and maintenance signals while keeping patient-safety checks visible. It is especially relevant for isolation rooms, operating rooms, ICUs, medical gas systems, and clinical HVAC workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as read-first/read-only but includes a high-impact BACnet write capability for clinical building systems.

Mitigation: Review it as a clinical control-system integration; require dry-run, approval, undo, authorization, and formal change control before any write, especially on life-safety-related HVAC or medical-gas systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured text with inline commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include worst-first clinical safety findings, protocol diagnostics, readiness gaps, approval guidance, and change-control context.]

## Skill Version(s):

0.23.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
