## Description: <br>
Clinical-facility edition of iaiops for hospital facility monitoring and analysis across BACnet/IP BMS, Modbus medical-gas panels and meters, OPC-UA plant SCADA, and cross-protocol safety checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, clinical facility teams, and authorized operators use this skill to inspect hospital BMS, medical-gas, SCADA, alarm, and maintenance signals and produce structured safety-oriented analysis. It is intended for read-first monitoring and triage in healthcare facilities, with any BACnet write use requiring authorization and change control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary flags a high-impact BACnet write action despite read-only clinical positioning. <br>
Mitigation: Install only for authorized users and connected MCP servers with permission to access the target hospital facility systems; require explicit approval and change control before any BACnet write action. <br>
Risk: Clinical facility analysis can be mistaken for the authoritative safety state of life-safety-related systems. <br>
Mitigation: Treat generated findings as structured analysis and verify them against site procedures, facility staff, medical-gas alarm panels, infection-control requirements, and applicable clinical safety controls before action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline commands and structured analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference facility readings, compliance checks, protocol diagnostics, and change-control steps; no raw scanner reinterpretation is included.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
