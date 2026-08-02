## Description: <br>
Process-industry edition of iaiops for chemical, pharmaceutical, food and beverage, and oil and gas plants, covering HART-IP process instrumentation, OPC-UA reads, Modbus-TCP/RTU, optional MQTT/Sparkplug B UNS, and cross-protocol diagnostics for downtime root cause, data quality, and OEE. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and process engineers use this skill to inspect process-plant telemetry across HART-IP, OPC-UA, Modbus, and optional MQTT/Sparkplug B, then generate diagnostic guidance for loop health, equipment fouling, data quality, downtime root cause, alarms, historian coverage, OEE, and compliance evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Use near live plant systems may affect historian pushes, stream publishing, exports, baseline updates, alias adoption, or Modbus-capable operations despite the skill's read-oriented framing. <br>
Mitigation: Require explicit operator approval, scoped configuration boundaries, and change-management review before enabling those operations. <br>
Risk: The skill describes MOC-gated write behavior for optional MQTT/Sparkplug use and includes publish/export surfaces that can move data beyond read-only diagnostics. <br>
Mitigation: Keep dry-run behavior enabled where available, require named approval before production writes or publishes, and verify target endpoints before execution. <br>
Risk: Industrial diagnostic outputs may be misleading if based on thin history, stale tags, bad-quality values, or unverified gateway behavior. <br>
Mitigation: Validate source data quality, quote underlying samples in diagnostic conclusions, and require engineering review before operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and text guidance with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first industrial diagnostics; write-capable publish, export, historian, baseline, alias, and Modbus-related operations require explicit operator approval and configuration boundaries.] <br>

## Skill Version(s): <br>
0.21.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
