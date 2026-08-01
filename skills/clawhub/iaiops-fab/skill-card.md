## Description: <br>
Fab edition of iaiops for semiconductor and display fab equipment over SECS/GEM and OPC-UA, providing read-first diagnostics, downtime root-cause support, OEE, asset inventory, data quality checks, SPC, and defect Pareto analysis with MOC-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, fab automation engineers, and operations teams use this skill to inspect SECS/GEM and OPC-UA equipment signals, triage downtime, analyze alarms, OEE, data quality, SPC, and defect Pareto results, and prepare controlled change workflows for semiconductor or display fab tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact industrial and data-export capabilities may be broader than the skill's read-only framing suggests. <br>
Mitigation: Before production fab installation, confirm that export, historian push, and stream publishing destinations are explicitly authorized. <br>
Risk: PLC write tools exposed through the fab profile could affect production equipment if controls are bypassed. <br>
Mitigation: Verify write tools are blocked or enforce dry-run defaults, undo capture, named approval, and double confirmation before any production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis, Code] <br>
**Output Format:** [Markdown with inline commands, tool names, configuration snippets, and analytical findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first workflow guidance; industrial write paths require MOC controls when exposed by the fab profile.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
