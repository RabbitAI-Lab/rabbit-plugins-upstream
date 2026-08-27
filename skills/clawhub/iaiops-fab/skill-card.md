## Description:

Fab edition of iaiops for semiconductor and display fab equipment over SECS/GEM and OPC-UA, supporting status reads, diagnostics, OEE, asset inventory, data quality checks, SPC, and defect Pareto analysis with read-first and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fab engineers use this skill to guide agents through semiconductor or display equipment diagnostics, SECS/GEM and OPC-UA status reads, data quality checks, OEE analysis, root-cause triage, SPC checks, and defect Pareto analysis. The skill emphasizes read-first operation and change-management gates for write-capable fab profile tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industrial data export, historian push, stream publish, and UNS publish capabilities may move sensitive fab data outside approved destinations.

Mitigation: Restrict export and publish destinations, credentials, and network egress; require explicit approval and audit logging before enabling these tools in production or regulated fab environments.

Risk: Write-capable fab profile tools can affect production equipment if change controls are bypassed.

Mitigation: Keep write actions behind dry-run defaults, named approvals, pre-change value capture, rollback plans, and post-change audit records.

Risk: Diagnostics and root-cause guidance may be incomplete or misleading if based on stale, unverified, or partial equipment signals.

Mitigation: Require responses to cite live or recorded signals, confirm GEM and OPC-UA connectivity first, and route production decisions through fab operating procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration]

**Output Format:** [Markdown with inline commands and tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should cite real signals for diagnostics and keep write actions behind dry-run, approval, audit, and rollback controls.]

## Skill Version(s):

0.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
