## Description:

Water-treatment edition of iaiops for waterworks, wastewater plants, and pump stations, covering Modbus-TCP/RTU, OPC-UA, HART-IP process instrumentation, and cross-protocol diagnostics for root-cause analysis, data quality, and OEE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Water-treatment engineers, OT teams, and agent developers use this skill to inspect water plant telemetry, assess water quality and compliance inputs, triage alarms and downtime, and draft read-first operational diagnostics across Modbus, OPC-UA, and HART-IP sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags a mismatch between read-only positioning and listed export, publish, push, and persistent baseline tools.

Mitigation: Review before installation in real water-treatment or OT environments and treat the skill as a mixed read/export/publish profile unless runtime controls prove those tools are disabled or gated.

Risk: Export and publish behavior can move operational data outside intended systems if destinations are not controlled.

Mitigation: Require explicit approvals, destination allowlists, and least-privilege credentials before enabling any export, historian push, stream publish, or UNS publish workflow.

Risk: Water-treatment and OT diagnostics can affect high-consequence operational decisions if results are treated as control authorization.

Mitigation: Use outputs as reviewable diagnostic guidance and require site procedures, change-management approval, and qualified human review before production control changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-water)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured operational guidance with inline commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first diagnostics; evidence-linked compliance and investigation outputs when source data is provided]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
