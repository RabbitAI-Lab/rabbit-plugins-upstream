## Description:

A Chinese middle-school physics problem-solving coach that guides students through reading and diagramming, physics modeling, calculation, and verification before reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and tutoring agents use this skill to work through middle-school physics problems step by step, especially force diagrams, circuit analysis, optical paths, model selection, unit conversion, and answer checks. It is intended to coach the problem-solving process rather than immediately provide final answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may reach beyond current-session physics coaching into learner-profile archiving, wrong-answer handoff, reminders, or experiment-design support.

Mitigation: Restrict profile access to physics-relevant fields, require explicit student and guardian consent where applicable, route experiment-design requests to the lab coach, and require clear confirmation before archive or reminder actions.

Risk: Memory and parent-sharing features could expose student learning records outside the intended audience.

Mitigation: Honor profile, cross-skill sharing, reminder, and parent-sharing consent fields; keep work in the current session when consent is absent; support review, correction, deletion, pause, and export controls.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [物理四步解题法状态机定义](references/physics-4step-statemachine.md)
- [物理苏格拉底三层次追问适配指南](references/physics-socrates-guide.md)
- [四类物理图景绘制追问手册](references/physics-diagram-guide.md)
- [物理意图识别模板](references/claw-templates-physics.md)
- [学习档案数据契约](shared/dna-profile.schema.json)
- [多智能体交接协议](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese tutoring guidance in Markdown-style text, with structured handoff or reminder configuration only after user confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce staged hints, diagram instructions, formula checks, generated practice items, and consent-gated handoff records.]

## Skill Version(s):

2.1.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
