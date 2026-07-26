## Description: <br>
Iaiops Process helps agents inspect process-industry plant telemetry across HART-IP, OPC-UA, Modbus, and optional Sparkplug/MQTT contexts for instrumentation health, downtime root cause, data quality, OEE, alarm, asset, and loop-health analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reliability engineers, and process-plant operators use this skill to guide read-first diagnostics and analysis for plant telemetry, instrumentation health, downtime root cause, OEE, alarms, and data quality across HART-IP, OPC-UA, and Modbus environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Industrial-control use may involve unclear write, export, or stream-publish authority despite read-first guidance. <br>
Mitigation: Require documented read-only enforcement, operator approval, dry runs, and management-of-change controls before use in production or safety-relevant systems. <br>
Risk: Historian, export, and stream-publish workflows may move sensitive plant telemetry outside expected boundaries. <br>
Mitigation: Review destinations, credentials, and data scope before enabling export or publish workflows, and restrict access to approved operators and systems. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/iaiops-process) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Analysis, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with tool names, environment variables, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first guidance for industrial telemetry; may include approval-gated write precautions when Sparkplug/MQTT publishing is in scope.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
