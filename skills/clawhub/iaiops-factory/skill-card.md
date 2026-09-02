## Description:

Factory edition of iaiops for discrete-manufacturing troubleshooting across PLC, CNC, servo and drive bus, tag browsing, Unified Namespace, OEE, downtime root-cause, asset inventory, and read-first industrial protocol workflows with MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and authorized industrial-operations teams use this skill to inspect and troubleshoot discrete-manufacturing systems across factory protocols, production data, asset models, alarms, OEE, and program-change baselines. Write-capable actions are intended to remain gated by management-of-change review, dry-run checks, approval, and rollback planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact write tools can affect industrial control systems when enabled.

Mitigation: Keep write tools disabled unless the operator has authorization, a real MOC process, named approval, dry-run review, and a rollback plan.

Risk: Factory-network access, raw-socket use, root privileges, or API tokens may broaden operational exposure.

Mitigation: Restrict privileges and tokens to the specific factory network, gateway, and assessment scope.

Risk: Troubleshooting advice may influence production-line decisions.

Mitigation: Use the skill only in environments where the operator is authorized to inspect or control industrial systems and review recommendations before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration notes, and structured troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve read-first posture, cite concrete operational evidence where available, and distinguish advisory analysis from approved control actions.]

## Skill Version(s):

0.26.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
