## Description:

Factory edition of iaiops helps agents inspect and troubleshoot discrete-manufacturing lines across PLC, CNC, fieldbus, MES/SCADA, MQTT/Sparkplug B, and Unified Namespace environments with read-first diagnostics and change-control-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial operations engineers use this skill to connect an agent to factory systems, read operational data, diagnose dataflow and downtime issues, build asset inventories, analyze OEE, and prepare controlled write proposals for production equipment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an agent to industrial automation systems can expose live operational technology environments to unintended actions.

Mitigation: Install only for intended industrial automation use, use dedicated OT network access for raw-socket protocols, and validate site readiness before connecting to live equipment.

Risk: High-impact write tools could change PLC, fieldbus, MQTT, or station configuration if enabled without governance.

Mitigation: Keep write tools disabled by default and require a real change-control process, named approval, dry-run review, and rollback planning before any production write.

Risk: Misconfigured secrets or approval gates could allow unauthorized access to MES, SCADA, broker, or controller interfaces.

Mitigation: Verify secret-store configuration, network scope, and approval gates before using the skill on live equipment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, configuration values, command examples, diagnostics, and structured operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first behavior is expected; write actions are high-impact and should remain disabled unless an explicit change-control process approves them.]

## Skill Version(s):

0.27.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
