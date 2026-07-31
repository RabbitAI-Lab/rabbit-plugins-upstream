## Description: <br>
Warehouse and intralogistics skill for analyzing conveyors, sorters, palletizers, AS/RS systems, AGV/AMR fleets, industrial protocol telemetry, predictive maintenance, downtime triage, OEE, throughput, and alarms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and industrial operations engineers use this skill to inspect warehouse automation telemetry, diagnose downtime and dataflow issues, evaluate bottlenecks and sortation health, and support predictive maintenance workflows across common industrial protocols. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents a read-first or read-only posture while documenting write or publish capabilities for industrial systems. <br>
Mitigation: Treat it as write-capable, install it only where industrial-system access is intended, verify broker/topic ACLs and PLC permissions, and confirm dry-run, named approval, undo, and double-confirmation controls before use near production equipment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline tool names, configuration values, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include industrial telemetry analysis, diagnostic recommendations, protocol-specific read operations, and proposed write actions that require authorization.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
