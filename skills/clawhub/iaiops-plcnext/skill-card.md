## Description:

Guides PLCnext and virtual-PLC diagnostics using OPC-UA and Modbus-TCP data for downtime, predictive maintenance, alarms, and OEE analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial engineers and developers use this skill to inspect PLCnext controller data and investigate equipment health, downtime, and production performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims a read-only surface but also describes export, publish, historian push, and file-writing tools.

Mitigation: Verify that the deployed runtime profile disables those tools before treating the skill as read-only; require approval and restricted write directories for any enabled outputs.

Risk: Stream, UNS, or historian outputs may send operational data outside the local environment.

Mitigation: Confirm destinations and data-sharing permissions before enabling publishing or historian outputs.

## Reference(s):

- [iaiops-plcnext on ClawHub](https://clawhub.ai/zw008/skills/iaiops-plcnext)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration instructions]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic findings, operational summaries, and setup guidance.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
