## Description:

Helps water-treatment operators and engineers inspect plant telemetry, assess water quality, and investigate equipment and data-quality issues across Modbus, OPC UA, and HART devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Waterworks and wastewater operators, engineers, and developers use the skill to review instrument readings and alarms, check treatment thresholds, investigate downtime, and prepare operational reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite its read-only description, some tools can create local files or publish plant telemetry to external destinations.

Mitigation: Allowlist read and write directories, review historian and publish destinations, and require approval before exports or pushes involving plant data.

Risk: Automated water-quality and compliance assessments may be mistaken for approved site limits or operational decisions.

Mitigation: Confirm site-specific thresholds and required CT values with responsible personnel before acting on results.

## Reference(s):

- [iaiops-water on ClawHub](https://clawhub.ai/zw008/skills/iaiops-water)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Files]

**Output Format:** [Text and structured tool results, with optional reports and exported files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes telemetry summaries, anomaly and root-cause assessments, threshold checks, and optional evidence bundles.]

## Skill Version(s):

0.32.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
