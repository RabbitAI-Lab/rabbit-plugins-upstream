## Description:

初中数学应用题的"文字→方程"专项，帮助学生用数量关系三步提取法识别量、用中文说关系，并把关系翻译成等式。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-support agents use this skill to coach middle-school math word problems where the blocker is translating text into equations. It focuses on guided modeling for travel, work-rate, concentration, profit, and growth-rate problems, then hands off equation solving or unrelated topics to other skills.

### Deployment Geography for Use:

China mainland by default; other regions require localized crisis resources, curriculum alignment, and minor-consent/privacy review before student use.

## Known Risks and Mitigations:

Risk: Crisis and student-safety resources are written for a mainland China Chinese K12 context.

Mitigation: Before use in other regions, localize emergency and youth-support channels and ask for the learner's country or region when location is unclear.

Risk: The skill can rely on OCR and learning-profile memory for minors.

Mitigation: Enable consent, privacy, view/correct/delete, pause-memory, and sharing controls before using persistent profiles or cross-skill sharing.

Risk: Generated practice questions or worked examples may contain incorrect or unsuitable math content.

Mitigation: Apply the included self-solve and item-check protocol before presenting generated items, and require teacher review before adding generated items to resource banks or tests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-word-problem-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [五大应用题题型建模框架与数量关系速查表](references/modeling-patterns.md)
- [提示阶梯与完整示例出口](shared/hint-ladder.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外](shared/crisis-exception.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [AI 出题自检协议](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, text, configuration]

**Output Format:** [Conversational Markdown or plain text tutoring guidance, with occasional structured handoff/configuration snippets for compatible learning-profile workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses short guided prompts, hint-ladder escalation, same-type worked examples, OCR fallback text, and optional learning-profile controls when platform memory is enabled.]

## Skill Version(s):

2.1.12 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
