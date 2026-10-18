## Description:

Helps renewable-site operators examine solar and wind telemetry, investigate underperforming PV strings, and assess alarms, downtime, and energy use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Renewable-site operators and engineers use this skill to review inverter and turbine data, triage performance and downtime issues, and analyze half-hourly electricity meter files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes itself as read-only but includes telemetry publishing capabilities.

Mitigation: Confirm whether the installed edition is read-only; require operator approval and allowlists before enabling MQTT, UNS, stream, or historian publishing in live environments.

Risk: Report and export tools can write host files.

Mitigation: Require operator approval and restrict report and export writes to approved directories.

## Reference(s):

- [iaiops-renewables on ClawHub](https://clawhub.ai/zw008/skills/iaiops-renewables)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration guidance]

**Output Format:** [Text and structured tool results; optional HTML meter report via CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Performance ratios and meter summaries cite inputs; missing meter readings are not treated as zero.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
