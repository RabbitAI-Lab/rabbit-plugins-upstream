## Description:

iaiops-fab helps agents work with semiconductor and display fab equipment across SECS/GEM and OPC-UA for read-first diagnostics, status discovery, alarms, OEE, asset inventory, data quality, and root-cause analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Fab automation, manufacturing, and equipment-interface engineers use this skill to inspect SECS/GEM and OPC-UA equipment signals, analyze alarms and downtime, and prepare evidence-backed operational guidance while keeping production writes gated by change approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for fab and industrial-control environments and references write-capable factory tools, so unauthorized or poorly controlled production access could affect equipment operations.

Mitigation: Install only for authorized users and confirm MOC approval, dry-run behavior, and deployment safeguards before enabling production access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool-call recommendations, command examples, and structured analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first fab and industrial-control guidance; production writes require external MOC approval controls.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
