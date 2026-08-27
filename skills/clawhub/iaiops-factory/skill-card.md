## Description:

Factory edition of iaiops for discrete-manufacturing operations across PLC, CNC, servo and drive bus, tag browsing, Unified Namespace, production-line troubleshooting, downtime root-cause analysis, OEE, and asset inventory workflows with read-first behavior and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation engineers, and operations teams use this skill to inspect and troubleshoot discrete-manufacturing lines across industrial protocols, SCADA/MES read layers, MQTT/Sparkplug B/UNS, and cross-protocol diagnostics. It supports advisory analysis, asset inventory, OEE and downtime workflows, and tightly controlled write paths that require MOC approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers high-impact factory-control capabilities and may be used around industrial control or production data.

Mitigation: Install only where the operator is authorized to access those systems, and keep write-capable tools disabled unless formal MOC approval, dry-run review, rollback planning, and network isolation are in place.

Risk: EtherCAT, PROFINET, publishing, and export workflows can affect raw networks or move operational data outside the source system.

Mitigation: Pay special attention to raw network access and publishing or export tools; restrict them to approved networks and reviewed data-transfer paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first industrial operations guidance with explicit approval gates for high-impact write actions.]

## Skill Version(s):

0.23.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
