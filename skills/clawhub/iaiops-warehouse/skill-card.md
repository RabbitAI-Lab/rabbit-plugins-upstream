## Description: <br>
Warehouse-focused iaiops skill for agents supporting intralogistics diagnostics across EtherNet/IP, Profinet, Modbus, OPC-UA, and MQTT-Sparkplug, including predictive maintenance, downtime triage, throughput, bottleneck, and alarm analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation engineers, and warehouse operations teams use this skill to guide read-first diagnostics, telemetry analysis, and maintenance triage for conveyors, sorters, palletizers, AS/RS systems, and AGV/AMR fleets. Any industrial write or publish action should be treated as a separately approved change-control step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents read-only positioning while documenting high-impact industrial write capabilities. <br>
Mitigation: Install only where industrial writes are explicitly allowed, keep writes dry-run by default, require human approval, and scope targets to approved control systems. <br>
Risk: The skill can support data egress through MQTT publishing, historian pushes, streams, and exports. <br>
Mitigation: Restrict broker, historian, stream, and export destinations to approved endpoints and review payload contents before enabling publication or export. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse) <br>
- [Source skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline tool names, shell commands, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include industrial diagnostic recommendations and proposed read, write, publish, export, or historian actions that require review before execution.] <br>

## Skill Version(s): <br>
0.21.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
