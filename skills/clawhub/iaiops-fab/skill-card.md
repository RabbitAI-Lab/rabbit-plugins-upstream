## Description:

iaiops-fab helps agents inspect semiconductor and display fab equipment across SECS/GEM, OPC-UA, and related industrial protocols for diagnostics, OEE, asset inventory, and data quality, with read-first workflows and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, fab operations engineers, and reliability teams use this skill to triage equipment connectivity, alarms, downtime, OEE, data quality, asset inventory, SPC, and defect Pareto workflows across SECS/GEM, OPC-UA, and related industrial-control interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fab equipment data, historian exports, baseline records, and investigation records can be operationally sensitive.

Mitigation: Install only in trusted fab environments, connect only to trusted iaiops MCP endpoints, and limit access to users authorized to inspect the relevant equipment data.

Risk: Production write-capable S7 and Modbus tools can affect industrial equipment if used without change control.

Mitigation: Keep MOC approval, dry-run defaults, undo values, named approver confirmation, and review steps enabled before any non-dry-run production write.

Risk: Diagnostics can be misleading when site readiness, connectivity, or source signal coverage is incomplete.

Mitigation: Run readiness and doctor checks first, prefer read-only SECS/GEM and OPC-UA evidence collection, and review advisory outputs before operational action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with diagnostic summaries, tabular analyses, tool-use recommendations, and command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include evidence-based references to inspected equipment signals and approval-gated recommendations for production writes.]

## Skill Version(s):

0.23.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
