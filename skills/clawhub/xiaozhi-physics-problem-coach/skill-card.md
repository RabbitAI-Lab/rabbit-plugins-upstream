## Description:

初中物理解题教练，按四步法（读题画图→物理建模→列式计算→检验反思）陪学生走完当前这一道物理题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and tutoring agents use this skill to guide Chinese middle-school physics problem solving through diagramming, modeling, calculation, and reflection for a specific current problem. It keeps long-term profile reads, wrong-answer handoff, and reminders optional and consent-gated.

### Deployment Geography for Use:

China mainland context by default; adapt local minor-consent, safety-channel, and curriculum assumptions before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill is intended for a Chinese middle-school physics tutoring context and may be used with minors.

Mitigation: Review local minor-consent requirements and keep profile reads, wrong-answer handoff, and reminders behind the documented consent gates.

Risk: Optional profile, handoff, and reminder behavior could expose or retain learning data if enabled too broadly.

Mitigation: Limit profile reads to physics weakness fields, require per-action confirmation for handoff and reminders, and honor view, correction, deletion, pause, sharing-control, and export requests.

Risk: A learner may disclose self-harm, abuse, severe despair, or other safety concerns during tutoring.

Mitigation: Stop the tutoring flow, state the AI boundary, encourage contact with a trusted adult or local emergency help, and avoid recording sensitive crisis details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [物理四步解题法 · 状态机定义](references/physics-4step-statemachine.md)
- [物理苏格拉底三层次追问适配指南](references/physics-socrates-guide.md)
- [四类物理图景绘制追问手册](references/physics-diagram-guide.md)
- [物理意图识别模板（CLAW 内部化）](references/claw-templates-physics.md)
- [DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Conversational Markdown with step-by-step tutoring prompts, textual diagram guidance, and optional handoff or reminder payload guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No hidden execution; optional profile read, wrong-answer handoff, and reminder enqueue require explicit consent.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
