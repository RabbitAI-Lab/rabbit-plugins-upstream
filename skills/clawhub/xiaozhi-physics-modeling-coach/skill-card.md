## Description:

初中物理建模教练，用三步法训练学生先识别物理现象、选择合适模型，再把模型表达成数学关系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and tutoring agents use this skill to practice junior-high physics modeling: identifying the phenomenon in a problem, choosing among core mechanics, pressure, buoyancy, circuits, and energy models, and forming the matching mathematical expression. It is suited for guided practice and model-transfer coaching rather than full problem solving or experiment design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep a physics modeling profile and enqueue study reminders when consent controls permit.

Mitigation: Require receiver-side authorization so writes are limited to subjectExtensions.physics.modelingProfile and reminders are enqueued only when profile sharing, reminder consent, and per-interaction agreement are present.

Risk: Generated practice prompts or modeling guidance may be pedagogically wrong or exceed the declared junior-high scope.

Mitigation: Use the bundled item self-check and scope rules before presenting generated exercises; label high-school-only content and avoid expanding it unless the student explicitly asks.

## Reference(s):

- [Physics Modeling Patterns Reference](references/physics-modeling-patterns.md)
- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-modeling-coach)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational Markdown with structured modeling prompts and optional consent-gated handover JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate practice prompts, model-selection guidance, profile update handoffs, and reminder enqueue handoffs when consent controls permit.]

## Skill Version(s):

2.1.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
