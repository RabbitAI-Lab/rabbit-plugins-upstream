## Description:

A Chinese junior-high math tutoring skill that guides students through single math problems, corrections, similar practice questions, and short pre-exam review using stepwise prompts instead of giving answers first.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and tutoring assistants use this skill to coach Chinese junior-high math problem solving, wrong-answer review, same-type practice, and near-term exam review. It is designed for external K12 tutoring contexts where records, reminders, and sharing are used only after the student or guardian has enabled the relevant consent settings.

### Deployment Geography for Use:

China mainland-style K12 tutoring contexts; localize consent, guardian, and emergency-response rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Minor-student data, parent sharing, reminders, and cross-skill records may be inappropriate without valid consent for the student's age and region.

Mitigation: Confirm student and guardian consent settings before enabling records, reminders, parent-visible summaries, or cross-skill handoffs; otherwise keep support in the current conversation.

Risk: The tutoring flow could be misused during an active exam or restricted assessment.

Mitigation: When a student says an exam or quiz is in progress, do not explain, hint, or solve the item; ask them to return after the assessment for review.

Risk: Generated same-type math questions can be incorrect, ambiguous, or off-grade without checking.

Mitigation: Use the bundled item self-check before presenting generated practice, and avoid persisting teacher-facing generated items unless a human has verified them.

Risk: Crisis or severe distress signals require support beyond math tutoring, and emergency contact guidance can be wrong outside the intended region.

Mitigation: Stop the tutoring flow on crisis signals, refer to trusted adults and local emergency resources, and localize emergency numbers before use outside Chinese mainland contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [数学四步拍照法状态机](artifact/references/photo-4step-statemachine.md)
- [数学苏格拉底五问链学段适配指南](artifact/references/math-socrates-guide.md)
- [意图分支扩展话术与苏格拉底五问各学段适配指南](artifact/references/claw-templates-extended.md)
- [提示阶梯与完整示例出口](artifact/shared/hint-ladder.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [交接协议 JSON Schema](artifact/shared/handover-protocol.schema.json)
- [危机例外](artifact/shared/crisis-exception.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational tutoring responses, structured study summaries, generated practice questions, and consent-gated handoff JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce wrong-answer handoff or reminder-queue records only when the required consent gates are satisfied; otherwise it stays within the current conversation.]

## Skill Version(s):

2.3.0 (source: ClawHub release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
