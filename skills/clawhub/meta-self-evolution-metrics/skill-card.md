## Description:

A distilled meta-skill for self-evolution metrics that adds self-verification, reflection, super-agent orchestration, adversarial validation, and a persistent learner loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to evaluate self-evolution workflows, recommend improvement actions, and record usage patterns for later reflection. It is intended for agents that need traceable self-checking and iterative improvement behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to keep cross-session usage memory and preferences.

Mitigation: Use only where persistent local memory is acceptable, and review stored learned_patterns.json data before sharing or packaging the skill.

Risk: The skill describes self-evolution behavior that may change future agent guidance.

Mitigation: Manually review any proposed SKILL.md updates or disable automatic instruction updates before deployment.

Risk: The authoritative security verdict is suspicious because the skill asks agents to evolve behavior without clear user control.

Mitigation: Install only after review, keep changes auditable, and require explicit user approval for behavior-changing updates.

## Reference(s):

- [Distillation report](artifact/distillation_report.md)
- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-self-evolution-metrics)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May record local usage patterns and preferences when the bundled learner workflow is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
