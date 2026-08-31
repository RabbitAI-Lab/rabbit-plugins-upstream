## Description:

PLCnext and virtualized-PLC edition of iaiops for reading Phoenix Contact PLCnext Control and vPLC data over built-in OPC-UA and Modbus-TCP services, with cross-protocol diagnostics for dataflow, downtime root cause, predictive maintenance, OEE, alarms, and baselines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial engineers use this skill to route PLCnext and virtualized PLC tasks to existing OPC-UA and Modbus tools for read-first diagnostics, health checks, alarm analysis, downtime triage, and operational reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents itself as read-only, but the security summary notes tools that can export data, publish events, push historian data, or create investigation records.

Mitigation: Review enabled backend tools before installation and disable or approval-gate any non-read-only actions.

Risk: Device-read diagnostics can expose operational data from PLCnext or virtualized PLC environments.

Mitigation: Install only in environments where data access is authorized and where approvals, network controls, and logging are enforced.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-plcnext)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline tool names, shell commands, and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first PLCnext profile guidance for OPC-UA, Modbus-TCP, diagnostics, and operational analysis workflows]

## Skill Version(s):

0.23.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
