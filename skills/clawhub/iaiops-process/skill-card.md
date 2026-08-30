## Description:

iaiops-process helps agents support process-industry diagnostics across HART-IP instrumentation, OPC-UA reads, Modbus devices, optional MQTT/Sparkplug UNS workflows, data quality, downtime root-cause analysis, and OEE with read-first and MOC-gated write posture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and operations teams use this skill to guide read-first investigation of process plants, including HART-IP instrument checks, OPC-UA or Modbus data access, alarm and downtime triage, data quality review, and evidence-based investigation workflows. Any write-adjacent publishing or export workflow should be reviewed under management-of-change controls before use on live or production-adjacent networks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read-only claims conflict with documented write-capable Modbus coverage.

Mitigation: Confirm Modbus write function codes are rejected by default before installation or use in any live plant or production-adjacent network.

Risk: Export, historian push, stream publish, UNS, MQTT, or Sparkplug workflows may move plant data or affect connected systems if under-scoped.

Mitigation: Require explicit destination allowlists, named approvals, audit logging, and management-of-change review for any publish or export workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, text]

**Output Format:** [Markdown guidance with inline commands and structured operational recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve read-first posture, cite supplied plant evidence where applicable, and surface approval requirements for write-adjacent actions.]

## Skill Version(s):

0.23.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
