## Description: <br>
Iaiops Fab helps agents inspect semiconductor and display fab equipment over SECS/GEM and OPC-UA, combining equipment status, alarms, recipes, OEE, asset inventory, data quality, and downtime root-cause workflows with a read-first, MOC-gated write posture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Fab engineers, automation engineers, and operations teams use this skill to investigate SECS/GEM and OPC-UA equipment state, alarms, recipes, downtime, quality signals, and cross-protocol asset context in semiconductor or display fabs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Industrial write, export, and publish capabilities can affect production equipment or move fab data outside intended destinations. <br>
Mitigation: Disable write, export, and publish tools unless they are required; require explicit approvals, destination allowlists, and dry-run review before enabling higher-impact actions. <br>
Risk: The documented MOC controls may not be enforced by the installed pip package implementation. <br>
Mitigation: Verify the installed implementation enforces the documented MOC controls before use in or near production fab systems. <br>
Risk: Diagnostic and root-cause guidance can be misleading when equipment, MES, alarm, or historian signals are incomplete. <br>
Mitigation: Review results against current fab context and corroborate recommendations with real equipment signals before operational action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured diagnostic results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include bounded samples, cited signal values, configuration checks, and MOC-gated action guidance.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
