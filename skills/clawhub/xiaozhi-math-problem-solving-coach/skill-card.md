## Description:

A Chinese-language middle-school math coaching skill that helps students work through individual math problems with stepwise questions, graduated hints, similar practice, and short pre-exam review when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and learning assistants use this skill to coach middle-school math problem solving in Chinese. It asks what the student has tried, gives limited stepwise hints before full explanations, verifies understanding with similar problems, and supports exam review only when the student explicitly requests it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A nonresponse path can archive a student's learning data after silence.

Mitigation: Remove or override that path before installation; when a student does not respond, close with a brief summary only unless current-turn consent to record is verified.

Risk: Profile reads, cross-skill sharing, reminders, or persistent records could expose student data without current consent.

Mitigation: Require clear current-turn consent and the relevant consent flags before reading, writing, sharing, or enqueueing reminders; require guardian consent where applicable.

Risk: Wrong-answer handovers could be accepted based on JSON schema validity alone.

Mitigation: Receiving agents should reject wrong-answer handovers unless crossSkillSharing is currently verified true and the handover authorization is checked independently.

Risk: Student math conversations may include crisis signals that exceed tutoring scope.

Mitigation: Stop tutoring flows when crisis signals appear and follow the bundled crisis-referral protocol, recording only the minimal disposition fact when an authorized profile already exists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [qizhitang publisher profile](https://clawhub.ai/user/qizhitang)
- [数学四步拍照法状态机](artifact/references/photo-4step-statemachine.md)
- [数学苏格拉底五问链学段适配指南](artifact/references/math-socrates-guide.md)
- [意图分支扩展话术与苏格拉底五问各学段适配指南](artifact/references/claw-templates-extended.md)
- [提示阶梯与完整示例出口](artifact/shared/hint-ladder.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Conversational Chinese text and Markdown, with optional JSON handover objects for approved cross-skill transfers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are constrained by hint-ladder levels, short IM-style turn budgets, current-turn consent gates, and crisis-referral rules.]

## Skill Version(s):

2.1.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
