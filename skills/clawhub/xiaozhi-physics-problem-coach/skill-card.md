## Description:

A Chinese K12 physics tutoring agent that guides middle-school through first-year high-school students through a four-step problem-solving flow: draw the physical situation, model it, calculate, then verify and reflect.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and tutors use this skill to work through a specific Chinese K12 physics problem with Socratic hints, diagram-first reasoning, model selection, calculation checks, and reflection. It is designed for current-session tutoring by default, with learning-record handoff or reminders only after explicit consent.

### Deployment Geography for Use:

Global, with localization required outside Chinese K12 tutoring contexts.

## Known Risks and Mitigations:

Risk: The skill is tailored to a Chinese K12 tutoring context and may be inappropriate if language, curriculum assumptions, crisis resources, or minor-consent rules do not match the deployment setting.

Mitigation: Localize the tutoring content and safety resources before deployment outside the intended context, and confirm applicable minor-consent requirements.

Risk: Learning-record memory, cross-skill sharing, wrong-answer archiving, and reminders can affect student privacy if enabled without the required consent gates.

Mitigation: Confirm the platform enforces explicit consent before profile memory, cross-skill sharing, wrong-answer archiving, or reminders are enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [物理四步解题法状态机定义](artifact/references/physics-4step-statemachine.md)
- [四类物理图景绘制追问手册](artifact/references/physics-diagram-guide.md)
- [物理意图识别模板](artifact/references/claw-templates-physics.md)
- [物理苏格拉底追问指南](artifact/references/physics-socrates-guide.md)
- [高一必修第一册样板题](artifact/references/physics-hs1-worked-examples.md)
- [Learning DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, json]

**Output Format:** [Chinese conversational tutoring text with occasional Markdown structure and consent-gated JSON handoff records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Current-session tutoring by default; optional profile reading, wrong-answer handoff, and reminders require explicit consent.]

## Skill Version(s):

2.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
