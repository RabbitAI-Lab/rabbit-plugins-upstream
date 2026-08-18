## Description:

Assess whether to escalate models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to decide when model escalation is justified, how to investigate before escalating, and how to document the reasoning behind a model or effort-level change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms may cause this advisory skill to appear during adjacent agent, orchestration, or governance conversations.

Mitigation: Review and narrow the trigger list if tighter activation behavior is required.

Risk: Escalation guidance can influence model-selection decisions even though the skill is documentation-only.

Mitigation: Treat the output as advisory and require human or orchestrator review for high-cost or high-stakes escalation decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-escalation-governance)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with checklists, tables, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only advisory output; no tool access or persistent actions are requested.]

## Skill Version(s):

1.9.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
