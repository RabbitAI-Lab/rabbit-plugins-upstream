## Description:

Warehouse and intralogistics skill for agents working with conveyors, sorters, palletizers, AS/RS, AGV/AMR fleets, industrial protocols, predictive maintenance, downtime triage, OEE, throughput, and alarm analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial operations engineers and warehouse automation teams use this skill to inspect warehouse material-handling systems, analyze telemetry, triage downtime, assess throughput and OEE, and prepare guarded operational actions. The evidence flags that the release describes itself as read-only while also documenting write and publish tools, so production use should require authorization, gating, logging, and non-production testing first.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release claims a read-only posture while documenting write and publish operations that could affect warehouse control systems or operational data flows.

Mitigation: Treat the skill as mixed read/write in production contexts; require separate authorization, gating, logging, and successful non-production testing before any write or publish operation.

Risk: Use in a production or safety-sensitive warehouse environment could affect material-handling operations if actions are approved without operational review.

Mitigation: Have qualified site personnel review proposed actions and limit production execution to approved maintenance-of-change workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational analysis, diagnostic next steps, tool recommendations, and guarded command guidance.]

## Skill Version(s):

0.23.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
