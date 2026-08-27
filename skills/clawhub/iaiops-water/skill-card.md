## Description:

Water-treatment edition of iaiops for waterworks, wastewater plants, and pump stations, supporting read-oriented Modbus, OPC-UA, HART-IP, water-quality, compliance, diagnostics, asset-health, and operational analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Water and wastewater operators, OT engineers, and developers use this skill to read plant telemetry, diagnose dataflow and downtime, assess data quality, and generate water-quality or compliance-oriented analysis from Modbus, OPC-UA, and HART-IP systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the artifact is framed as read-only but exposes export, historian push, and publish-style tools without enough warning or scoping.

Mitigation: Disable or gate export, historian push, and publish tools behind explicit user approval, destination allowlists, and audit logging before use.

Risk: The security evidence marks the release suspicious for use around real water, wastewater, SCADA, or plant networks.

Mitigation: Review the skill carefully before installation in operational environments and test it in a segregated non-production setting first.

Risk: Artifact behavior includes workflows related to plant operations, compliance, alarms, and diagnostics where incorrect guidance could affect operational decisions.

Mitigation: Require qualified operator review for recommendations, verify source measurements, and keep any production-control changes outside this skill unless separately approved through management-of-change procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-water)
- [Publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with inline tool names, shell commands, configuration notes, and operational analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compliance-style summaries, diagnostic findings, data-quality notes, and risk-aware operational recommendations based on user-provided or read-only plant data.]

## Skill Version(s):

0.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
