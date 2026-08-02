## Description: <br>
Water-treatment edition of iaiops for read-first Modbus, OPC-UA, and HART-IP operations, including water quality checks, downtime root-cause analysis, data quality watchdogs, and OEE support for waterworks, wastewater plants, and pump stations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, water-treatment operations engineers, and reliability teams use this skill to guide read-first diagnostics, protocol data reads, water quality compliance checks, alarm and data-quality analysis, and downtime root-cause workflows for water and wastewater facilities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill claims a read-only water-treatment profile while documenting push, publish, export, baseline-learning, and alias-changing tools. <br>
Mitigation: Before installation or use, verify the actual MCP server profile disables, separately permissions, or approval-gates historian push, stream publish, export, baseline change, and alias adoption tools. <br>
Risk: Water-treatment and industrial-control recommendations can affect safety and compliance if treated as automatic operating instructions. <br>
Mitigation: Keep the workflow read-first, require authorized management-of-change review for any write-capable profile, and use dry-run, undo values, and named approval before production changes. <br>
Risk: Compliance calculations rely on caller-provided required CT values, permit limits, and site-specific thresholds. <br>
Mitigation: Use authorized site, state, or permit values as inputs and require cited input values before relying on compliance conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-water) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis] <br>
**Output Format:** [Markdown guidance with inline commands, tool names, and operational workflow steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first operational guidance for water-treatment diagnostics, protocol reads, compliance checks, and root-cause analysis.] <br>

## Skill Version(s): <br>
0.21.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
