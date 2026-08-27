## Description:

Warehouse and intralogistics skill for working with material-handling assets such as conveyors, sorters, palletizers, AS/RS systems, AGV/AMR fleets, WMS/WCS gateways, and related industrial telemetry across EtherNet/IP, Profinet, Modbus, OPC-UA, and MQTT-Sparkplug.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Warehouse automation, controls, and operations engineers use this skill to inspect warehouse control data, diagnose downtime and throughput issues, analyze alarms, and plan predictive maintenance for material-handling equipment. It is intended for read-first operational analysis, with production-changing actions handled only through explicit authorization and approval controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports that the skill claims a read-only posture while documenting production-impacting write and publish actions.

Mitigation: Use only where the IAIOPS MCP server enforces real authorization, dry-run defaults, approval gates, and environment scoping; disable or separate write and publish tools for deployments that must be read-only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, analysis]

**Output Format:** [Markdown with inline commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tool names, configuration notes, diagnostic workflows, and risk-aware operational guidance.]

## Skill Version(s):

0.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
