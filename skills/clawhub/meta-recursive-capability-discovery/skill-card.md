## Description:

Meta Recursive Capability Discovery helps agents identify missing capabilities for open-ended goals, add self-verification and reflection checks, and record lessons for iterative improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to compare required capabilities against existing skills, identify decomposable and leaf capability gaps, and audit blind spots before adding new skills or orchestration steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner script can record local notes across sessions when used.

Mitigation: Review or disable learner behavior when cross-session skill state is not desired.

Risk: The skill is framed for self-improving capability discovery and may be connected to memory, reflection, or super-agent systems.

Mitigation: Require explicit approval before connecting it to any super-agent, memory, or reflection system.

## Reference(s):

- [Distillation report](artifact/distillation_report.md)
- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-recursive-capability-discovery)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Markdown guidance and structured JSON from the discovery script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local learner notes when the learner script is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
