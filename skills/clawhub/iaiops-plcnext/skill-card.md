## Description:

iaiops-plcnext helps agents operate a read-first PLCnext and vPLC monitoring workflow over OPC-UA and Modbus-TCP, with diagnostics, downtime root-cause analysis, PdM, OEE, alarms, baselines, data quality, onboarding, and investigation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial engineers use this skill to diagnose, monitor, and analyze Phoenix Contact PLCnext Control and vPLC environments through OPC-UA and Modbus-TCP without adding a PLCnext-specific connector. It supports read-first OT observability, onboarding, root-cause analysis, data-quality, compliance-evidence, and baseline workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is framed as read-only, but the evidence security summary notes documented export, publish, historian-push, UNS, baseline-persistence, and history functions.

Mitigation: Review before production OT installation and require explicit approval, verified destinations, least-privilege credentials, and data-classification checks before using export, publish, historian-push, UNS, baseline, or history functions.

Risk: Using the skill in production OT environments can affect sensitive process data flows even when PLC process access is read-only.

Mitigation: Treat PLC process access as read-only, verify all external data destinations, and apply site change-control and approval processes for any workflow that persists, exports, publishes, or pushes data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-plcnext)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, analysis]

**Output Format:** [Markdown guidance with inline commands, tool names, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce reports, scorecards, evidence bundles, and configuration drafts for read-first PLCnext/vPLC workflows over OPC-UA and Modbus-TCP.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
