## Description: <br>
Process-industry edition of iaiops for chemical, pharma, food and beverage, and oil and gas plants, covering HART-IP process instrumentation, OPC-UA DCS/gateway reads, Modbus-TCP/RTU assets, optional MQTT/Sparkplug B UNS workflows, and cross-protocol diagnostics for root cause, data quality, and OEE. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, process engineers, and plant operations teams use this skill to inspect process-instrumentation and plant-data workflows across HART-IP, OPC-UA, Modbus, and optional Sparkplug/UNS paths. It supports read-first diagnostics for dataflow, alarms, historian health, asset modeling, loop health, heat-exchanger fouling, downtime root cause, data quality, and OEE. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary flags tension between read-only claims and data-publishing or possible write-capable behavior. <br>
Mitigation: Review the skill before production or plant-connected installation, confirm Modbus writes are disabled, and require explicit approval for historian export, push, or stream publishing. <br>
Risk: Plant diagnostics and generated guidance could be incorrect or misleading if used without operational review. <br>
Mitigation: Use outputs as diagnostic support, review them with qualified plant personnel, and scan the skill before deployment. <br>
Risk: Optional MQTT/Sparkplug publishing can affect external systems if enabled without controls. <br>
Mitigation: Keep publishing workflows dry-run or approval-gated by default, require named authorization, and limit targets to intended non-production or approved production systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tool names, workflow steps, shell commands, and configuration environment variables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first process diagnostics; optional publishing or write-like workflows should remain explicitly approved and scoped to intended systems.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
