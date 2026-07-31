## Description: <br>
Clinical-facility edition of iaiops for hospital building systems, combining BACnet/IP, Modbus, OPC-UA, and cross-protocol diagnostics for isolation-room pressure, medical-gas, operating-room environment, asset, alarm, data-quality, and maintenance analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and facilities engineers use this skill to inspect hospital BMS, medical-gas, SCADA, alarm, historian, and maintenance signals across BACnet/IP, Modbus, and OPC-UA. It is suited to read-first clinical-facility triage and compliance-oriented analysis, with BACnet write actions requiring separate approval and technical controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence states that the skill claims read-only behavior while documenting a high-impact BACnet write capability for hospital building systems. <br>
Mitigation: Treat the skill as write-capable; use it only where BACnet writes are technically gated, approval-controlled, asset-scoped, logged, and prohibited for life-safety systems unless formally authorized. <br>
Risk: Clinical-facility checks can surface patient-safety-relevant pressure, gas, ventilation, and alarm findings that may be incomplete or dependent on source point quality. <br>
Mitigation: Use the findings as structured analysis for qualified review, and confirm safety-critical decisions against site procedures, authoritative alarms, and authorized clinical-facility personnel. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or text guidance with inline tool and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include clinical-facility risk rankings, cited point readings, protocol-specific next steps, and approval-gated write guidance.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
