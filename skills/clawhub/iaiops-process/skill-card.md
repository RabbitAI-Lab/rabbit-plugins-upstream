## Description:

Process-industry edition of iaiops for chemical, pharma, food and beverage, and oil and gas plants, helping agents read HART-IP, OPC-UA, Modbus, and optional MQTT/Sparkplug B UNS signals for process instrumentation, downtime root-cause analysis, data quality, and OEE with a read-first, MOC-gated posture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and process engineers use this skill to guide agents through process plant data collection and analysis across HART-IP, OPC-UA, Modbus, and optional UNS/Sparkplug workflows. It supports loop health, heat exchanger fouling checks, alarm and data quality analysis, OEE, downtime triage, asset modeling, investigation workflows, and configuration drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact historian, export, stream publish, or UNS publish operations may affect operational data if enabled without clear approval gates.

Mitigation: Confirm the enabled toolset and require explicit human approval before any operation that exports, publishes, or writes operational data.

Risk: Production plant installation may carry elevated operational risk because the scanner classified the release as suspicious.

Mitigation: Review the skill before production use and install dependencies only in a contained environment with pinned, verified packages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process)
- [Publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code]

**Output Format:** [Markdown guidance with tool names, command snippets, configuration drafts, and structured analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose historian, export, stream publish, or UNS publish operations; production-impacting actions require review and explicit approval gates.]

## Skill Version(s):

0.28.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
