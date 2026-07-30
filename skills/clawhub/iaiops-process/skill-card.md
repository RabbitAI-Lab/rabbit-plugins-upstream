## Description: <br>
iaiops-process guides agents through process-industry diagnostics across HART-IP, OPC-UA, Modbus, optional MQTT/Sparkplug B UNS, and cross-protocol analysis for root cause, data quality, and OEE. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, plant engineers, and operations teams use this skill to guide read-first diagnostics for process plants using HART-IP instruments, OPC-UA gateways, Modbus devices, and cross-protocol health, root-cause, data-quality, compliance, and OEE workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is intended for high-consequence plant contexts and mixes read-only diagnostics with write, publishing, and data-export capabilities. <br>
Mitigation: Review before installing in production or plant-connected environments, and confirm historian push, export_data, stream publishing, and Sparkplug/MQTT publishing are disabled, dry-run, or explicitly approval-gated unless those actions are intended. <br>
Risk: Plant data export or stream publishing could move operational data beyond the intended boundary. <br>
Mitigation: Allow export and publishing only after confirming the destination, approval path, and operational need for the specific deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands and tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is framed for read-first process diagnostics, with optional publishing or data movement requiring explicit review and gating.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
