## Description:

Assess whether to escalate models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to decide when model escalation is justified, how to document the trade-off, and when to investigate before changing model capability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model escalation guidance can affect cost and latency when agents choose stronger or higher-effort models.

Mitigation: Review the skill against organizational model routing, budget, and latency policies before deployment.

Risk: Misapplied escalation guidance can lead to unnecessary escalation or insufficient escalation for high-stakes decisions.

Mitigation: Require agents to document the escalation reason, scope, and success criteria, and keep human review for high-stakes workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-escalation-governance)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides decision criteria, escalation protocol guidance, and model capability notes; it does not execute code or access data.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
