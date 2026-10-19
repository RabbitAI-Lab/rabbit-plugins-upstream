## Description:

Supports hospital facilities teams with cross-protocol monitoring, diagnostics, and advisory safety checks for isolation rooms, medical gases, and operating-room conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Hospital facilities engineers and operators use the skill to inspect BACnet, Modbus, and OPC-UA readings, prioritize potential isolation-room and medical-gas issues, and investigate equipment alarms. Clinical safety checks are advisory; local alarms and facility procedures remain authoritative.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The read-first description may obscure a BACnet write capability affecting clinical infrastructure.

Mitigation: Require site change control and named approval, keep dry-run enabled by default, and never issue unauthorized commands to life-safety systems.

Risk: Publishing and exporting operational data can disclose facility information or write outside intended locations if configured broadly.

Mitigation: Govern publishing and exports under site policy and restrict configured read and write directories to approved paths.

Risk: Incorrect sensor data or advisory checks could mislead patient-safety decisions.

Mitigation: Verify readings against local facility alarms and follow clinical and facilities procedures for safety decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/iaiops-clinical)
- [Publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Text and structured analysis, with optional reports and exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings reference measurements and prioritize severe deviations; some workflows can publish data or write files.]

## Skill Version(s):

0.31.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
