## Description:

Water-treatment edition of iaiops for read-first diagnostics and analysis across Modbus-TCP/RTU, OPC-UA, and HART-IP waterworks, wastewater plant, pump station, and process instrumentation environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and operations teams use this skill to inspect water-treatment telemetry, diagnose dataflow and downtime issues, check water-quality thresholds, and produce evidence-backed operational analysis without directly commanding plant equipment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents the water edition as read-only while also listing export, publish, and historian-push capabilities that could move operational data.

Mitigation: Before installation in a plant or utility environment, confirm those actions are unavailable in the water profile or gated by explicit operator approval and audit logging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-water)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited readings, threshold comparisons, change-baseline summaries, and operator review guidance.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
