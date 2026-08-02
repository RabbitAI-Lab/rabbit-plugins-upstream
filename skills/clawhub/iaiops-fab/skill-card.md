## Description: <br>
iaiops-fab helps agents monitor and analyze semiconductor or display fab equipment across SECS/GEM and OPC-UA, including downtime root-cause support, OEE, asset inventory, and data-quality workflows with a read-first, MOC-gated write posture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, fab automation engineers, and operations teams use this skill to guide agent work on SECS/GEM, OPC-UA, PLC-adjacent diagnostics, downtime root-cause analysis, OEE, asset inventory, and fab data-quality tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Export, stream-publishing, or PLC-write tools could affect production systems or move fab data to unintended destinations. <br>
Mitigation: Use the skill only where fab equipment access is intended, and confirm destination controls, MOC approval, dry-run defaults, undo capture, and named approvals before production use. <br>
Risk: Operational recommendations for root-cause analysis or equipment health could be misleading if treated as automatic decisions. <br>
Mitigation: Review outputs against real equipment signals and site procedures before taking corrective action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with inline commands and tool-selection guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first operational guidance; write-capable paths are described as MOC-gated with dry-run and undo expectations.] <br>

## Skill Version(s): <br>
0.21.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
