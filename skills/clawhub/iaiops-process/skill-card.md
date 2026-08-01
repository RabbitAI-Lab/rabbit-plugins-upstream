## Description: <br>
Process-industry edition of iaiops for chemical, pharma, food and beverage, and oil and gas plants; it guides agents through read-first diagnostics across HART-IP instruments, OPC-UA, Modbus TCP/RTU, optional MQTT/Sparkplug B, downtime root-cause analysis, data quality, and OEE. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, process engineers, and plant operations teams use this skill to guide read-first diagnostics for process instrumentation, control-loop health, data quality, downtime root cause, historian coverage, and compliance evidence workflows. It is intended for process plants using HART-IP, OPC-UA, Modbus TCP/RTU, and optionally MQTT/Sparkplug B. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Export and publishing tools may move plant data or publish events without sufficiently explicit scoping. <br>
Mitigation: Require destination allowlists, explicit approvals, and audit logging before enabling historian_push, export_data, stream_publish, or stream_publish_event near real plant data. <br>
Risk: Use in production or sensitive plant environments may exceed the security posture described by the release evidence. <br>
Mitigation: Review the skill before installation and enforce read-first operation plus management-of-change controls for any write-capable integration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured guidance with inline commands and tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance emphasizes read-first diagnostics, cited values, approval gates for write-capable integrations, and plant-data export restrictions.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
