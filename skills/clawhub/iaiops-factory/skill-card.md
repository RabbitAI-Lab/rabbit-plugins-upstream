## Description: <br>
Factory edition of iaiops for discrete-manufacturing lines, covering OPC-UA, Modbus-TCP/RTU, Siemens S7comm, Mitsubishi MC/MELSEC, Omron FINS, Allen-Bradley EtherNet/IP, EtherCAT, PROFINET discovery, MTConnect, IO-Link, MQTT/Sparkplug B/UNS, and cross-protocol factory troubleshooting for downtime root cause, OEE, and asset inventory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation engineers, and factory operations teams use this skill to inspect PLC, CNC, servo and drive bus, tag browse, Unified Namespace, MES/SCADA, and production-line evidence, then perform root-cause, OEE, asset-inventory, data-quality, and compliance workflows. The skill is read-first, with high-impact control-system writes requiring MOC approval, dry-run behavior, and undo data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward high-impact factory control-system write operations. <br>
Mitigation: Keep write tools disabled by default, require named MOC approval, use dry runs, capture backups or undo data, and avoid production credentials unless operating inside a governed industrial network. <br>
Risk: Factory diagnostics may depend on live operational technology access, raw-socket privileges, or protocol-specific network reachability. <br>
Mitigation: Install only where the agent is intentionally authorized to inspect factory systems, and avoid raw-socket or production network privileges outside governed industrial environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis, Markdown, Code] <br>
**Output Format:** [Markdown with inline commands, tool recommendations, configuration guidance, and structured diagnostic analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include read-first factory diagnostics, protocol-specific tool selection, risk-gated write guidance, and evidence-backed root-cause or OEE summaries.] <br>

## Skill Version(s): <br>
0.21.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
