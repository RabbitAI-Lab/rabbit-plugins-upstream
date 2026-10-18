## Description:

Helps process-plant engineers read industrial instrumentation data and investigate data quality, equipment health, and downtime across HART-IP, OPC-UA, and Modbus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Process-plant engineers and operators use this skill to inspect instrument readings and diagnose alarms, data quality, equipment health, and downtime before deciding on operational actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Export or historian push may expose plant data outside approved locations.

Mitigation: Require explicit operator approval and restrict exports to approved directories and historian endpoints.

Risk: Stream or UNS publishing and evidence-bundle creation may have high-impact effects without consistent approval controls.

Mitigation: Review proposed publishing and bundle destinations, and require explicit approval before executing these actions in production or regulated environments.

## Reference(s):

- [iaiops-process on ClawHub](https://clawhub.ai/zw008/skills/iaiops-process)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Human-readable analysis and procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide configuration drafts and recommendations for follow-up actions.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
