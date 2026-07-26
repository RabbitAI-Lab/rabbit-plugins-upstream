## Description: <br>
Iaiops Warehouse helps agents inspect and analyze warehouse and intralogistics operations across EtherNet/IP, Profinet, Modbus, OPC-UA, and MQTT-Sparkplug telemetry, including predictive maintenance, downtime triage, OEE/throughput, alarms, bottlenecks, and sortation health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and operations teams use this skill to guide warehouse and material-handling diagnostics, telemetry analysis, predictive maintenance, throughput/OEE review, alarm analysis, and controlled OT change workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is flagged suspicious because it presents a read-only posture while exposing write-capable control-system tools. <br>
Mitigation: Review before installing in any warehouse or industrial network; enable it only where write-capable tools are technically gated, approved, logged, and separated from production unless explicitly authorized. <br>
Risk: Write-capable OT operations such as EtherNet/IP tag writes and Profinet DCP changes can affect warehouse or industrial equipment if executed without authorization. <br>
Mitigation: Keep dry-run, approval, audit, and change-management gates enabled; restrict credentials and network access to approved maintenance contexts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, analysis] <br>
**Output Format:** [Markdown guidance with inline commands, configuration notes, and tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include OT diagnostics, read/write gating guidance, and risk notes.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
