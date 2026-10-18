## Description:

Helps water and wastewater operators inspect instrument readings, investigate equipment downtime and data quality, and assess water-treatment compliance across Modbus, OPC-UA, and HART-IP sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Waterworks and wastewater operators and their engineers use this skill to review plant telemetry, diagnose faults and alarm patterns, and prepare water-quality and compliance assessments. Confirm site-specific thresholds and approve any export or publication of operational data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite read-only wording, enabled tools can export or write reports and publish data to historian, stream, or UNS destinations.

Mitigation: Review enabled tools, restrict writable directories and network destinations, and require operator approval before operational or compliance data leaves the environment.

Risk: Water-quality and disinfection assessments can be misleading if default thresholds or supplied CT requirements do not match local permits and operating conditions.

Mitigation: Have qualified operators check site-specific limits, input readings, and required CT values before using assessments for compliance decisions.

## Reference(s):

- [iaiops-water ClawHub release](https://clawhub.ai/zw008/skills/iaiops-water)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration instructions, Reports]

**Output Format:** [Text and Markdown; configuration drafts and report files where enabled]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available plant data and operator-supplied compliance limits.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
