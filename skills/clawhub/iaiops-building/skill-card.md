## Description:

Building automation skill for BACnet/IP, Modbus, IO-Link, MQTT, and BAS controller workflows, including discovery, point and trend reads, diagnostics, facility checks, and approval-gated write commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, building automation engineers, and facility operators use this skill to inspect HVAC/BMS systems, collect point and trend evidence, diagnose dataflow and alarm issues, and prepare controlled actions for BACnet, BAS, MQTT, and related building telemetry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad OT data movement and non-building analysis functions without clear gating in the skill text.

Mitigation: Review the skill before installing in a live facility environment and confirm export, historian, stream, and UNS publishing tools are disabled, destination-limited, audited, or approval-gated according to site policy.

Risk: Commands can affect live building automation equipment if write paths are enabled.

Mitigation: Keep BACnet, BAS, and MQTT write commands in dry-run mode unless authorized through the documented MOC and approval workflow, and separately confirm live facility permissions before use.

Risk: PLC file analysis and fleet/compliance functions may be outside the intended scope for some building deployments.

Mitigation: Confirm that these functions are intended for the target site before enabling them or relying on their outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-building)
- [Publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, shell commands, configuration settings, and risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-first workflows and approval-gated write guidance for building automation contexts]

## Skill Version(s):

0.23.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
