## Description:

Renewables edition of iaiops for solar PV plants and wind farms, covering inverter and combiner telemetry, wind-turbine controllers, plant SCADA, MQTT-Sparkplug telemetry, predictive maintenance, downtime and alarm analysis, and underperforming-string detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect renewable-energy telemetry, investigate underperforming PV strings, review wind-farm and plant SCADA health, triage downtime and alarms, and prepare evidence-oriented operational summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents itself as read-first/read-only while documenting publish, push, and export tools that can modify or disclose operational data.

Mitigation: Install with a read-only MCP/tool policy by default, and enable publishing, pushing, or exporting only for explicit tasks with destination allowlists and user confirmation.

Risk: Use in real plant, SCADA, MQTT, UNS, or historian environments could affect sensitive operational systems or data flows.

Mitigation: Review the skill before installation in operational environments and stage it against non-production or read-only connections before authorizing access to live systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-renewables)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text with tool names, commands, configuration notes, and analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference site telemetry, protocol diagnostics, baseline comparisons, and security-sensitive publish/export actions when the connected tool policy permits them.]

## Skill Version(s):

0.26.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
