## Description:

Helps warehouse operations teams analyze equipment telemetry, downtime, throughput, alarms, and maintenance needs across industrial protocols.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Warehouse operators and industrial engineers use this skill to investigate conveyor, sorter, and mobile-robot performance, diagnose downtime, and plan maintenance from equipment and WMS/WCS data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes itself as read-only but documents industrial write actions and message publishing that can affect warehouse systems.

Mitigation: Allow read access by default; block write and publish tools unless separately approved, and require change-control review before any production action.

## Reference(s):

- [iaiops-warehouse on ClawHub](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown and structured diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include asset health assessments, bottleneck findings, downtime analyses, and maintenance recommendations.]

## Skill Version(s):

0.29.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
