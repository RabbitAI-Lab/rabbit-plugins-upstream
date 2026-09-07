## Description:

初中物理建模教练，用三步法（识别现象、选择模型、数学表达）帮助学生先判断物理模型再列式。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, tutors, and learning-support agents use this skill to coach junior-high physics modeling: identifying the physical phenomenon, choosing an appropriate core model, and expressing the model mathematically before practice or transfer.

### Deployment Geography for Use:

China Mainland by default; other regions require localization of curriculum assumptions, emergency-resource guidance, and minor-consent requirements.

## Known Risks and Mitigations:

Risk: The skill can read consent/profile metadata, write a physics learning profile, and queue study reminders after consent.

Mitigation: Keep memory and reminders off unless needed, require explicit consent before profile writeback or reminder queueing, and limit shared data to the physics modeling fields documented in the bundled schemas.

Risk: The security summary notes that profile and reminder data contracts are broader and less tightly validated than necessary for the declared junior-high modeling scope.

Mitigation: Review integrations before deployment, narrow accepted reminder types and handover fields where possible, and prefer versions with tighter schemas.

Risk: The artifact is designed for a China Mainland Chinese K12 context and includes region-specific curriculum, emergency-resource, and minor-consent assumptions.

Mitigation: Localize curriculum scope, emergency guidance, and consent requirements before serving learners in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-modeling-coach)
- [Physics modeling patterns](references/physics-modeling-patterns.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational Markdown with optional structured handover records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce consent-gated learner-profile updates and reminder-queue payloads; generated practice items are expected to pass the bundled self-check protocol.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
