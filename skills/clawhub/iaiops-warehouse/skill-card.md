## Description:

iaiops-warehouse helps agents inspect, diagnose, and analyze warehouse and intralogistics operations across EtherNet/IP, Profinet, Modbus, OPC-UA, and MQTT-Sparkplug telemetry, including predictive maintenance, downtime triage, throughput/OEE, alarm analysis, bottleneck detection, and sortation health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and operations teams use this skill to guide read-first warehouse automation diagnostics, telemetry review, OEE and throughput analysis, alarm analysis, predictive maintenance, and onboarding for material-handling systems. The skill also documents write-capable industrial operations tools that require explicit change-management approval and scoped permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is described as read-first or read-only in places, while evidence.security reports documented write and publishing tools that could affect control systems or operational data.

Mitigation: Review it as a write-capable industrial operations skill; install only where PLC, Profinet, MQTT, historian, stream, and export permissions are intentionally scoped and approvals are technically enforced.

Risk: Unpinned or environment-mismatched industrial protocol package versions can change behavior in operational environments.

Mitigation: Pin package versions for the target environment and validate protocol behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline commands, tool names, configuration guidance, and operational analysis steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run write procedures, approval prerequisites, and evidence-oriented diagnostic steps.]

## Skill Version(s):

0.28.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
