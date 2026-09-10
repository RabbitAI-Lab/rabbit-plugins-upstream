## Description:

Warehouse and intralogistics edition of iaiops for agents working with conveyors, sorters, AS/RS, AGV/AMR fleets, WMS/WCS gateways, and cross-protocol predictive maintenance, downtime, OEE, throughput, and alarm analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and warehouse automation or OT engineers use this skill to inspect protocol data, diagnose throughput and downtime issues, analyze alarms, and produce maintenance-oriented guidance for material-handling assets. Any write or publish action should be treated as controlled change work requiring site authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags a mismatch between the skill's read-only wording and documented write or publish capabilities for industrial systems.

Mitigation: Deploy as read-mostly, restrict production network access, and require site authorization, dry runs, change approval, and approval controls before any write or publish action.

Risk: Warehouse automation and OT interactions can affect production equipment if used without local controls.

Mitigation: Use only in authorized warehouse automation contexts with network containment and site-specific change-management procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-warehouse)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with inline tool names, shell commands, analysis summaries, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first posture; high-impact write or publish actions require external authorization, dry runs, change approval, and network containment.]

## Skill Version(s):

0.27.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
