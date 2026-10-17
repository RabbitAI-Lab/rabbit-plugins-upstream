## Description:

Helps engineers diagnose PLCnext and virtualized PLC operations through OPC UA and Modbus data, including downtime, alarms, equipment health, and OEE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial engineers and operators use this skill to inspect PLCnext or virtualized PLC data, investigate downtime and alarms, and assess equipment health and OEE. Review any proposed exports or publishing actions before use in a production environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The claimed read-only profile also lists export, publish, historian-push, report, and evidence-bundle capabilities whose side effects are unclear.

Mitigation: Review the skill before industrial installation; clarify or remove these capabilities from the read-only edition, or document their side effects and require explicit approval before use.

## Reference(s):

- [iaiops-plcnext on ClawHub](https://clawhub.ai/zw008/skills/iaiops-plcnext)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Tool results and human-readable diagnostic guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic findings, alarm analysis, OEE metrics, and configuration drafts.]

## Skill Version(s):

0.29.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
