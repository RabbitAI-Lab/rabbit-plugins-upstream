## Description:

iaiops-renewables helps agents analyze renewable-energy telemetry from solar PV plants and wind farms across Modbus, OPC-UA, and MQTT-Sparkplug, including PV underperformance, predictive maintenance, downtime, OEE, alarm, and data-quality workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, plant engineers, and operations teams use this skill to inspect renewable-energy site telemetry, assess PV string and inverter performance, triage downtime and alarms, and draft onboarding or configuration guidance for industrial data systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill claims a read-only posture while listing publish and push tools that could alter external telemetry systems.

Mitigation: Review the skill before installation in live OT, SCADA, MQTT, historian, or UNS environments; use read-only credentials where possible and avoid production broker publish permissions.

Risk: Publish, push, baseline, snapshot, or declaration operations may affect operational records or downstream analysis if used without review.

Mitigation: Require explicit human approval before any publish, push, baseline, snapshot, or declaration operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-renewables)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON-like analysis results, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference industrial telemetry, protocol endpoints, alarm histories, asset models, baselines, and investigation records supplied by the user or connected tools.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
