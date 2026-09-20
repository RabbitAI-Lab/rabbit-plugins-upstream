## Description:

Renewables edition of iaiops for solar PV plants and wind farms, covering Modbus-connected inverters, string combiners, wind-turbine controllers, OPC-UA plant SCADA, MQTT-Sparkplug telemetry, cross-protocol diagnostics, predictive maintenance, downtime, OEE, alarms, and PV underperformance analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reliability engineers, and operations teams use this skill to inspect renewable energy site telemetry, diagnose underperforming PV strings or inverters, triage wind-farm and plant SCADA issues, and draft read-first onboarding or configuration guidance for supported industrial protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports a mismatch between read-only positioning and listed operations that can publish, push, or export operational data.

Mitigation: Before production OT installation, restrict credentials and broker or historian permissions to the intended mode, and require explicit operator approval or tool-side allowlists for any publish, push, or export operation.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first workflow guidance; production OT use requires review of tool permissions and credentials before enabling publish, push, or export operations.]

## Skill Version(s):

0.28.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
