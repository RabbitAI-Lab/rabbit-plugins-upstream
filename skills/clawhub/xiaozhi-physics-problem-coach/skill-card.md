## Description:

面向初中到高一学生的中文物理解题教练，引导学生按读题画图、物理建模、列式计算、检验反思四步完成当前一道物理题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and education agents use this skill for Chinese-language K12 physics problem coaching. It guides one current physics problem at a time, with optional consent-gated profile lookup, wrong-answer handoff, and reminder handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Minor learners may require guardian consent before profile access, cross-skill sharing, wrong-answer archiving, or reminders.

Mitigation: Enable profile lookup, sharing, archival handoff, and reminder handoff only after the platform verifies the applicable consent gates.

Risk: A physics tutoring response could be treated as help during an active exam or restricted assessment.

Mitigation: When the student indicates an active exam or test, decline to solve or hint on the current problem and offer post-exam review instead.

Risk: Self-harm, abuse, bullying, or severe distress signals are outside the learning-support scope.

Mitigation: Stop normal tutoring, state the AI boundary, encourage contact with trusted adults or local emergency resources, and avoid recording sensitive details beyond the permitted referral fact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [物理四步解题法 · 状态机定义](references/physics-4step-statemachine.md)
- [四类物理图景绘制追问手册](references/physics-diagram-guide.md)
- [物理苏格拉底三层次追问适配指南](references/physics-socrates-guide.md)
- [高一必修第一册样板题](references/physics-hs1-worked-examples.md)
- [物理意图识别模板](references/claw-templates-physics.md)
- [档案 schema](shared/dna-profile.schema.json)
- [交接协议 schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown-style tutoring guidance with optional structured handoff instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language tutoring responses; optional wrong-answer and reminder handoff payloads only after explicit consent.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
