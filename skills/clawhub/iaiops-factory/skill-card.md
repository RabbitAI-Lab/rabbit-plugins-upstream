## Description:

Factory edition of iaiops for discrete-manufacturing lines, covering OPC-UA, Modbus, Siemens S7comm, Mitsubishi MC/MELSEC, Omron FINS, Allen-Bradley EtherNet/IP, EtherCAT, PROFINET, MTConnect, IO-Link, MQTT/Sparkplug B/UNS, and cross-protocol analysis for downtime root cause, OEE, asset inventory, and production-line troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Factory engineers, automation developers, and operations teams use this skill to inspect industrial protocol endpoints, troubleshoot production-line dataflow and downtime, compute OEE signals, inventory assets, and prepare governed configuration drafts. Write-capable operations are intended to stay gated by management-of-change approval, dry-run behavior, and rollback procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable industrial control actions can affect PLCs, EtherCAT device state, PROFINET station configuration, or MQTT topics.

Mitigation: Keep production write tools disabled unless the site has explicit change-control approval, dry-run review, named approval, and rollback procedures.

Risk: Industrial protocol access may require privileged host or network access and can expose sensitive plant operations.

Mitigation: Install and run the skill in an isolated environment from a trusted package source with pinned and hash-verified dependencies.

Risk: Some live hardware, gateway paths, and site-specific protocol coverage require local verification before operational use.

Mitigation: Use the documented doctor-first and read-first workflows, validate discovered facts against site equipment, and avoid acting on unverified placeholders.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, structured findings, configuration drafts, and analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only industrial telemetry summaries, bounded scans, cited evidence chains, and gated write proposals.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
