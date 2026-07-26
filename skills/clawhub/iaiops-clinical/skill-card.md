## Description: <br>
Clinical-facility edition of iaiops for hospital building systems, medical-gas monitoring, OPC-UA plant SCADA, and patient-safety-oriented checks for isolation rooms, operating rooms, and medical gas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Hospital facilities engineers, clinical operations teams, and automation specialists use this skill to inspect BACnet, Modbus, and OPC-UA signals, prioritize patient-safety checks, and triage facility alarms or downtime. It supports read-first workflows for isolation-room pressure, operating-room environment, medical-gas source pressure, and related building-control diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is mostly documentation-only, but it claims read-only behavior while also documenting high-impact BACnet write capability for hospital building controls. <br>
Mitigation: Treat the skill as potentially write-capable; use it only where BACnet write access is intentionally allowed, external approval controls are enforced, and high-impact actions remain dry-run or explicitly approved. <br>
Risk: Hospital and clinical OT environments can affect patient safety, and the evidence says Modbus capabilities should be clarified before deployment. <br>
Mitigation: Review the skill carefully before installing in a hospital or clinical OT environment, verify Modbus behavior with the publisher, and rely on onsite clinical, facilities, and NFPA 99 controls for safety-critical decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline commands and structured operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include clinical-facility safety checks, protocol-specific tool recommendations, and approval-oriented guidance for write-capable BACnet actions.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
