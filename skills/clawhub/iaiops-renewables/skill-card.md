## Description:

Helps renewable-energy operators analyze solar and wind telemetry, investigate underperforming PV strings and equipment alarms, and review half-hourly electricity-meter data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Plant operators and engineers use the skill to inspect solar PV and wind-farm data across Modbus, OPC-UA and MQTT-Sparkplug, investigate performance and maintenance issues, and analyze site electricity consumption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite its read-only description, documented tools can publish or push operational data and write reports or exports.

Mitigation: Use read-only credentials by default; separately gate publish, push, export and report tools, restrict destinations and write directories, and require explicit user confirmation before MQTT, historian, stream, UNS or file-writing actions.

## Reference(s):

- [iaiops-renewables on ClawHub](https://clawhub.ai/zw008/skills/iaiops-renewables)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Shell commands]

**Output Format:** [Natural-language analysis and operational guidance with structured tool results where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include performance rankings, alerts, consumption summaries and suggested configuration; some documented tools can publish data or write files.]

## Skill Version(s):

0.32.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
