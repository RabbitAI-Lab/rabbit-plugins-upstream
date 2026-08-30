## Description:

Factory edition of iaiops for discrete-manufacturing troubleshooting across OPC-UA, Modbus, S7comm, MELSEC, FINS, EtherNet/IP, EtherCAT, PROFINET, MTConnect, IO-Link, MQTT/Sparkplug B/UNS, and cross-protocol diagnostics such as downtime root cause, OEE, and asset inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial automation engineers and site operators use this skill to inspect PLC, CNC, fieldbus, MES/SCADA gateway, Unified Namespace, and production-line data, then produce diagnostic guidance for root-cause analysis, OEE, asset inventory, readiness checks, and investigation records. Write-capable paths should be used only through explicit MOC approval in controlled environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact PLC and network capabilities could affect industrial operations if used outside an authorized change-management process.

Mitigation: Install only in controlled industrial environments, use read-only diagnostics first, and keep write tools disabled unless explicit authorization and MOC approval are in place.

Risk: Gateway or API credentials for MES, SCADA, or fieldbus access could expose sensitive operational systems if mishandled.

Mitigation: Store gateway and API credentials only in the intended secret store and avoid inline credential handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with inline shell commands and structured diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first diagnostics; write-capable actions require explicit MOC approval and default-disabled write tooling according to evidence.]

## Skill Version(s):

0.23.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
