## Description:

现代文阅读专项教练：先把文章真正读懂，再把话按阅卷规范说清楚，覆盖记叙文、散文、议论文、说明文、非连续性文本的读法与答题规范，并要求学生先尝试再获得提示或反馈。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, parents, teachers, and tutoring agents use this skill for Simplified Chinese K-12 modern-reading comprehension practice. It helps students read a passage first, diagnose recurring error patterns, revise answers against text evidence and scoring conventions, and preserve profile updates only with consent.

### Deployment Geography for Use:

China Mainland by default; localize curriculum assumptions, minor consent rules, and crisis referral resources before deploying elsewhere.

## Known Risks and Mitigations:

Risk: The skill is designed for minors and can update or share learning profile information when platform memory is enabled.

Mitigation: Use the disclosed profile controls for viewing, correction, deletion, pause, sharing, and export; require appropriate consent before profile writeback or cross-skill sharing.

Risk: Crisis referral guidance and curriculum assumptions are tailored to Mainland China.

Mitigation: Localize emergency resources, consent rules, grade bands, and scoring conventions before deploying outside Mainland China.

Risk: Reading-comprehension feedback can mislead students if it supplies answers before independent attempts or estimates scores without local rubrics.

Mitigation: Keep the documented hint ladder and evidence-based feedback flow: ask the student to try first, cite passage evidence, avoid score estimates, and use analogous examples instead of giving original answers prematurely.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-reading-decoder)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [语文错因维度表](references/chinese-error-dimension-table.md)
- [阅读五坑专项训练策略](references/pit-training.md)
- [现代文各题型出题逻辑与答题模板详解](references/question-type-library.md)
- [危机例外](shared/crisis-exception.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [提示阶梯与完整示例出口](shared/hint-ladder.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, configuration]

**Output Format:** [Markdown-style conversational tutoring guidance with structured feedback blocks and optional JSON-compatible handoff data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce consent-gated profile writeback or handoff payloads; does not execute code or install software.]

## Skill Version(s):

2.2.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
