## Description: <br>
Warehouse and intralogistics edition of iaiops for material-handling operations across conveyors, sorters, palletizers, AS/RS, AGV/AMR fleets, and related industrial telemetry protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and warehouse operations teams use this skill to guide read-first diagnostics, predictive maintenance, downtime triage, OEE/throughput analysis, alarm analysis, and controlled operational workflows for warehouse OT and IIoT systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill describes a read-first posture while documented tools can write PLC tags, change Profinet station settings, publish MQTT data, and export or push operational records. <br>
Mitigation: Deploy only under explicit site policy that separates read-only tasks from write, publish, and export paths, and require approval before any high-impact action. <br>
Risk: Use against warehouse OT and IIoT systems could affect production operations if write-capable paths are enabled without controls. <br>
Mitigation: Restrict credentials and network access to the minimum required scope, prefer dry-run behavior, and validate all operational changes through the site's change-management process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include operational analysis, workflow steps, and approval-oriented guidance for warehouse OT/IIoT tasks.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
