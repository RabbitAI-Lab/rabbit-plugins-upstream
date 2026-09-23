## Description:

初中到高一的物理建模教练，用识别现象、选择模型、数学表达的三步法训练学生先判断物理模型再列式。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, families, and education-focused agents use this skill to coach middle-school through first-year high-school physics modeling. It guides students to identify physical phenomena, choose an appropriate model, and express the model mathematically without substituting for full worked-solution tutoring.

### Deployment Geography for Use:

Global, with China-mainland curriculum assumptions and crisis-contact guidance localized before deployment outside mainland China.

## Known Risks and Mitigations:

Risk: The skill assumes Simplified Chinese, China-mainland K12 physics curriculum conventions and includes China-mainland crisis-contact defaults.

Mitigation: Localize curriculum scope and emergency or youth-support contact guidance before deploying outside mainland China.

Risk: Learning-profile memory, cross-skill sharing, parent sharing, and reminder handoffs can expose student learning data if enabled without the right consent posture.

Mitigation: Enable those features only when consent requirements are met, and honor the skill's view, correct, delete, pause, sharing-control, and export controls.

Risk: Student self-harm, abuse, bullying, or severe despair signals exceed the skill's tutoring scope.

Mitigation: Stop normal tutoring flow, avoid diagnosis, direct the student to trusted adults and localized emergency or support channels, and record only the referral fact when permitted.

Risk: Use during an active exam or test could enable academic misconduct.

Mitigation: When the student says an exam or test is in progress, do not explain that item or provide hints; offer post-exam review instead.

Risk: Generated practice items or model-transfer exercises may contain invalid, ambiguous, or out-of-scope physics content.

Mitigation: Run the included item self-check before presenting generated exercises and label teacher-facing generated items for human verification before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-modeling-coach)
- [physics-hs1-models.md](artifact/references/physics-hs1-models.md)
- [physics-modeling-patterns.md](artifact/references/physics-modeling-patterns.md)
- [platform-conventions.md](artifact/shared/platform-conventions.md)
- [crisis-referral-protocol.md](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown conversational tutoring guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce learning-profile summaries, handoff payload guidance, reminder requests, and safety referrals when the platform capabilities and user consent allow them.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
