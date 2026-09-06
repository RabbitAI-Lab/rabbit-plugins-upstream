## Description:

This skill coaches junior-high students through physics problems with a four-step flow: draw the physical situation, choose the model, calculate, and check the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and tutoring agents use this skill to work through a specific junior-high physics problem, especially force diagrams, circuit analysis, buoyancy, optics, and calculation checks. It stays in the current conversation by default and only uses memory, error-book handoff, or reminder handoff after explicit consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled schemas may expose more student profile data than the physics tutoring flow needs.

Mitigation: Limit deployment access to the stated consent fields, physics weak-point fields, and explicit handoff fields; block unrelated profile data before the skill receives context.

Risk: Emotional signals, safety records, or unrelated student context could be transferred through profile or handoff data.

Mitigation: Remove emotional-signal transfer from handoffs and keep crisis handling limited to referral behavior and minimal authorized disposition records.

Risk: Reminder behavior could be enabled without a validated reminder_enqueue contract or current user consent.

Mitigation: Keep reminders disabled unless reminderConsent is true, the student explicitly asks in the current session, and the reminder_enqueue schema is validated.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [SKILL.md](artifact/SKILL.md)
- [物理意图识别模板](artifact/references/claw-templates-physics.md)
- [物理四步解题法状态机定义](artifact/references/physics-4step-statemachine.md)
- [四类物理图景绘制追问手册](artifact/references/physics-diagram-guide.md)
- [物理苏格拉底三层次追问适配指南](artifact/references/physics-socrates-guide.md)
- [DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Conversational text or Markdown, with optional JSON handoff payloads when explicitly consented.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces stepwise tutoring prompts, diagram guidance, answer checks, and consent-gated handoff suggestions; no shell commands or code execution are expected.]

## Skill Version(s):

2.1.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
