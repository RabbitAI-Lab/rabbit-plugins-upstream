## Description: <br>
Factory edition of iaiops for discrete-manufacturing lines across OPC-UA, Modbus-TCP/RTU, Siemens S7comm, Mitsubishi MC/MELSEC, Omron FINS, Allen-Bradley EtherNet/IP, EtherCAT, PROFINET, MTConnect, IO-Link, MQTT/Sparkplug B/UNS, plus downtime root-cause, OEE, and asset-inventory workflows with read-first and MOC-gated write behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing engineers, controls engineers, and operations teams use this skill to inspect, troubleshoot, and analyze discrete-manufacturing PLC, CNC, gateway, UNS, and production-line data. It emphasizes read-first diagnostics and requires managed change approval for high-impact write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact write tools could affect production control systems if enabled without authorization. <br>
Mitigation: Keep write tools disabled by default, require formal management-of-change approval, verify dry-run behavior, and confirm undo or rollback data before any production write. <br>
Risk: Broad access to PLCs, gateways, brokers, and credentials can expand operational blast radius. <br>
Mitigation: Install only where industrial-control access is intended and restrict credentials and network reach to the specific devices, gateways, and brokers required for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, analysis] <br>
**Output Format:** [Markdown with inline shell commands and structured troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include protocol-specific tool names, diagnostic sequences, risk labels, and MOC-gated write guidance.] <br>

## Skill Version(s): <br>
0.22.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
