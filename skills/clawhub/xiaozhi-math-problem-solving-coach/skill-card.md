## Description:

A Chinese-language junior-high math problem-solving coach that guides students through math questions, wrong-answer review, similar-problem practice, and pre-exam review by asking scaffolded questions instead of immediately giving answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-assistant agents use this skill to work through junior-high math problems, diagnose where a solution got stuck, generate checked similar practice questions, and prepare for near-term exams. Deployers using it with minors should confirm learning-memory sharing, parent visibility, reminder behavior, retention, and local crisis-resource settings before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle minors' learning records, weak-point summaries, reminders, and cross-skill handoffs.

Mitigation: Confirm consent settings, parent visibility, retention rules, and cross-skill sharing controls before deployment.

Risk: Generated practice problems or math explanations could be incorrect or above the intended grade band.

Mitigation: Use the bundled AI item self-check process before presenting generated questions, and require review before adding generated items to durable resource banks.

Risk: Students may disclose self-harm, severe distress, bullying, or unsafe home situations during tutoring.

Mitigation: Stop the tutoring flow when crisis signals appear and follow the bundled crisis-referral protocol, including local emergency and youth-support resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [数学苏格拉底五问链学段适配指南](references/math-socrates-guide.md)
- [数学四步拍照法状态机定义](references/photo-4step-statemachine.md)
- [意图分支扩展话术与苏格拉底五问各学段适配指南](references/claw-templates-extended.md)
- [提示阶梯与完整示例出口](shared/hint-ladder.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机例外](shared/crisis-exception.md)
- [交接协议 schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, Configuration]

**Output Format:** [Conversational Markdown and structured handoff JSON when consented cross-skill transfer is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language tutoring responses with bounded hint levels, similar-question generation checks, consent-gated memory controls, and crisis-referral handling.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
