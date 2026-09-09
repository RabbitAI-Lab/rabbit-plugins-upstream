## Description:

Process-industry edition of iaiops for chemical, pharma, food and beverage, and oil and gas plants, covering HART-IP process instrumentation, OPC-UA, Modbus-TCP/RTU, optional MQTT/Sparkplug B UNS, downtime root-cause analysis, data quality, and OEE workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, plant engineers, and OT teams use this skill to inspect process-industry telemetry and evidence from HART-IP, OPC-UA, Modbus, historian, alarm, baseline, and investigation workflows. It supports read-first diagnostics for process instrumentation, data quality, downtime attribution, advisory matching, and controlled MOC-gated publishing workflows when optional Sparkplug paths are enabled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Export, push, publish, historian, UNS, MQTT, or Sparkplug paths could affect OT data flows if enabled without clear approval controls.

Mitigation: Review before installing in an OT environment; require disabled-by-default behavior or explicit approval, dry-run/review, scoped credentials, and audit logging for every publish or export path.

Risk: Baselines and evidence bundles may contain operational evidence whose retention, deletion, or export controls are unclear.

Mitigation: Confirm where baselines and evidence bundles are stored, who can access them, who can delete them, and how exports are controlled before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, analysis]

**Output Format:** [Markdown with tool names, configuration snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize read-first diagnostics, cited measurements, explicit unknown states, and review before OT deployment.]

## Skill Version(s):

0.27.0 (source: server release metadata, created 2026-09-03)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
