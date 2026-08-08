## Description: <br>
PLCnext and virtualized-PLC edition of iaiops for monitoring Phoenix Contact PLCnext Control and vPLC systems through built-in OPC-UA and Modbus-TCP interfaces, with cross-protocol diagnostics, downtime root cause analysis, predictive maintenance, OEE, alarm analysis, and baseline workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, automation engineers, and industrial operations teams use this skill to route PLCnext and virtual PLC monitoring tasks through standard OPC-UA and Modbus workflows. It helps inspect process data, diagnose connectivity or dataflow issues, analyze downtime and alarms, compute OEE, and review exported PLC program text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill describes a read-only PLC monitoring posture while also listing export, publish, evidence-bundling, stream, and historian write tools that can move industrial data outside the PLC environment. <br>
Mitigation: Before deployment, confirm the enabled runtime profile, disable nonessential export or publish tools, verify every non-local destination, and require approval gates for data movement. <br>
Risk: PLCnext and virtual PLC telemetry may include sensitive operational data. <br>
Mitigation: Limit access to approved operators, review exported or streamed data paths, and use least-privilege credentials for OPC-UA, Modbus, historian, and publishing integrations. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline command names, environment variables, and tool references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference OPC-UA, Modbus, PLC monitoring, export, publish, historian, and evidence-bundling tool behavior; the skill itself is documentation-only evidence.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
