## Description:

Guides read-first diagnostics and analysis of PLCnext and virtualized PLC systems through OPC UA and Modbus tools, including dataflow, downtime, alarms, maintenance, and OEE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Operations engineers and developers use this skill to inspect PLCnext or virtual PLC process data and investigate dataflow issues, downtime, alarms, and equipment health without changing controller settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A production MCP profile could expose write-enabled tools despite this edition's read-only intent.

Mitigation: Confirm the configured iaiops MCP profile is PLCnext/read-only before installation; review any export, historian, UNS, or approval-enabled write profile separately.

Risk: Broad file access could expose or modify operations files outside approved locations.

Mitigation: Limit IAIOPS_AGENT_READ_DIRS and IAIOPS_AGENT_WRITE_DIRS to approved operations folders.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration instructions]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings depend on available process data and site configuration; operators should validate conclusions before acting.]

## Skill Version(s):

0.32.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
