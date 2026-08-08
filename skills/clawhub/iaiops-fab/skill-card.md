## Description: <br>
Fab edition of iaiops for semiconductor and display fab equipment over SECS/GEM and OPC-UA, with cross-protocol support for downtime root-cause assistance, OEE, asset inventory, and data quality. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and fab automation engineers use this skill to guide agent work with SECS/GEM, OPC-UA, and related industrial data workflows for semiconductor or display equipment. It is intended for read-first diagnostics, quality analysis, OEE and downtime investigation, asset inventory, and controlled production-write workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide access to fab equipment and plant data, which may expose sensitive operational information or affect production environments. <br>
Mitigation: Install and use it only where the agent is authorized to access the relevant equipment, systems, and plant data. <br>
Risk: S7 or Modbus write paths can have production impact. <br>
Mitigation: Require documented approval, default dry-run behavior, undo information, and a named approver before any production write. <br>
Risk: Diagnostic and root-cause outputs may be advisory rather than definitive. <br>
Mitigation: Ground findings in real equipment signals and require operator or engineering review before acting on recommendations. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration notes, and structured operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should be grounded in observed tool data, cite signal sources when diagnosing equipment behavior, and keep production-write steps behind approval, dry-run, and undo controls.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
