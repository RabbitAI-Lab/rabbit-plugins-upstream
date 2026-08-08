## Description: <br>
Water-treatment edition of iaiops for read-first Modbus, OPC-UA, and HART-IP inspection, compliance checks, diagnostics, data quality, root-cause analysis, and OEE workflows in waterworks, wastewater plants, and pump stations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, integrators, and operations engineers use this skill to inspect water-treatment telemetry and diagnose plant, pump-station, analyzer, SCADA, and instrumentation issues across Modbus, OPC-UA, and HART-IP sources. It also supports compliance-oriented water-quality calculations, historian health checks, data-quality review, and root-cause analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The submitted evidence says the edition is read-only, while the documented tool inventory includes historian push, export, and stream publish capabilities. <br>
Mitigation: Before installation, confirm the runtime tool registry and remove or disable non-read-only tools unless explicit approval and destination controls are in place. <br>
Risk: Use in water utility or plant environments could expose operational data or affect operational workflows if export or publishing tools are available. <br>
Mitigation: Limit deployment to reviewed environments, enforce clear data-destination policy, and require operator approval for any tool that moves data outside the read path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-water) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration values, and tool-name references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first industrial water-treatment guidance; runtime tool availability should be reviewed before plant use.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
