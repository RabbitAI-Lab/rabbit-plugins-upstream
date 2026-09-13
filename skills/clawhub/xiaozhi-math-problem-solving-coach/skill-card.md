## Description:

Guides middle-school students through single math problems using staged hints, Socratic questions, similar practice problems, and exam review only when the student explicitly requests it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students use this skill to work through junior-middle-school math questions, find the step where they are stuck, and practice a similar problem after guidance. Agents can also use it for short exam-review sessions and consent-gated handoffs to related learning-record or reminder skills.

### Deployment Geography for Use:

Global, with crisis-support contacts and minor-data consent localized for the deployment region.

## Known Risks and Mitigations:

Risk: Minor student learning records could be read, archived, handed off, or used for reminders without sufficiently scoped consent.

Mitigation: Require explicit same-turn consent for every archive read, handoff, and reminder, and enforce crossSkillSharing and reminderConsent before routing any payload.

Risk: Cross-skill handoff payloads could be misrouted or contain undeclared fields.

Mitigation: Constrain recipients by handover type, validate payloads against the bundled handover schema, and reject undeclared payload fields.

Risk: Crisis-support handling can become unsafe when emergency contacts or minor-data practices are not localized.

Mitigation: Localize consent and crisis-support behavior for each deployment region; when the region is unknown, ask before giving phone numbers and provide only general emergency guidance.

Risk: AI-generated similar math problems may contain incorrect, ambiguous, or unsuitable items.

Mitigation: Apply the bundled AI item self-check before presenting generated problems and require human review before teacher-side resource-bank or exam use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [数学四步拍照法 · 状态机定义](references/photo-4step-statemachine.md)
- [数学苏格拉底五问链学段适配指南](references/math-socrates-guide.md)
- [意图分支扩展话术与苏格拉底五问各学段适配指南](references/claw-templates-extended.md)
- [提示阶梯与完整示例出口](shared/hint-ladder.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Plain Chinese text or Markdown, with structured JSON handoff records only after same-turn consent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses staged hint levels, short turn budgets, generated similar math problems, and consent-gated cross-skill handoff payloads.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
