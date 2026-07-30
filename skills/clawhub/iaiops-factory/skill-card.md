## Description: <br>
Factory edition of iaiops helps agents inspect and troubleshoot discrete-manufacturing systems across OPC-UA, Modbus, PLC, CNC, EtherCAT, PROFINET, MTConnect, IO-Link, MQTT/Sparkplug B, and MES/SCADA interfaces with read-first workflows and MOC-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Controls engineers, industrial operations teams, and developers use this skill to inspect production-line connectivity, troubleshoot downtime and data quality, inventory assets, compute OEE signals, and prepare governed control-system changes across common factory protocols. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthorized inspection of industrial systems could expose sensitive operational data or affect site governance. <br>
Mitigation: Install only in environments where the agent is authorized to inspect the target industrial systems. <br>
Risk: PLC, EtherCAT, PROFINET, and MQTT write paths can affect production systems. <br>
Mitigation: Keep write tools disabled unless a named change-approval process is in place, use dry-run behavior, preserve pre-change values for undo, and require explicit approval before writes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured operational recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first workflow guidance with dry-run and named approval expectations for high-impact writes.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
