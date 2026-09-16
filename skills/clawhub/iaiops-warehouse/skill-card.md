## Description:

Warehouse and intralogistics edition of iaiops for agents working with conveyors, sorters, palletizers, AS/RS, AGV/AMR fleets, WMS/WCS gateways, and industrial telemetry across EtherNet/IP, Profinet, Modbus, OPC-UA, and MQTT-Sparkplug.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to guide agents through warehouse industrial telemetry collection, diagnostics, predictive maintenance, bottleneck analysis, and incident investigation for material-handling systems. It is suited to read-first workflows over PLC, WMS/WCS, UNS, VFD, energy-meter, and fleet telemetry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims a read-only posture while documenting plant-control write actions and outbound publish/export tools.

Mitigation: Use read-only credentials by default and require human approval, destination allowlists, audited credentials, and pinned dependencies before enabling write or publish/export capabilities.

Risk: Use against warehouse industrial systems can affect operational safety, production flow, or sensitive telemetry handling if access is overbroad.

Mitigation: Install only for intended warehouse industrial environments, scope credentials to necessary assets, and review the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text guidance with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include industrial telemetry interpretation, tool names, safety posture, and approval gates; write actions should remain disabled unless explicitly authorized.]

## Skill Version(s):

0.28.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
