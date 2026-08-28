## Description:

iaiops-water helps agents inspect water-treatment operations through read-first Modbus, OPC-UA, and HART-IP workflows for instrumentation, data quality, root-cause analysis, OEE, and compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and engineers use this skill to guide monitoring, diagnostics, compliance checks, and incident investigation for waterworks, wastewater plants, pump stations, SCADA/PLC gateways, and process instrumentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact describes a read-only water-treatment profile while also listing external push, publish, historian push, and export capabilities.

Mitigation: Clarify or separate those capabilities from the read-only profile, and require explicit user approval, destination allowlists, and audit controls before operational use.

Risk: Operational guidance for water-treatment environments could affect safety, compliance, or incident response if used without site review.

Mitigation: Review the skill before installation in any operational environment and keep production-control changes behind the documented management-of-change process.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, configuration examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first operational guidance; production-control changes require separate approval controls outside this skill.]

## Skill Version(s):

0.23.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
