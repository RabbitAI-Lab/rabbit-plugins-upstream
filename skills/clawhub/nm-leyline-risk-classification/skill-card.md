## Description:

Classifies agent tasks into 4 risk tiers (GREEN/YELLOW/RED/CRITICAL).

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent orchestrators use this skill to classify code and configuration tasks by risk tier, decide verification gates, and mark tasks for safe sequencing or escalation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic triggers such as risk, safety, and verification may surface the skill during unrelated work.

Mitigation: Review the selected risk label in context and do not treat the GREEN default as a substitute for judgment on security, data, or production changes.

Risk: Heuristic classification can miss context that changes the true impact of a task.

Mitigation: Escalate uncertain work manually, use reversibility scoring for RED or CRITICAL tasks, and require human approval for CRITICAL work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-risk-classification)
- [Leyline homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance with risk-tier labels, task metadata examples, and verification checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; no commands, API calls, or secret access.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
