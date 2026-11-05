## Description:

为初高中学生提供按五层难度定位并逐级进阶的数学练习，同时支持经同意后整理训练记录和检测提醒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆初高中学生，用于评估已掌握知识点的当前练习层级，并循序练习更有挑战性的数学题。

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: Optional learning records can contain a student's performance history and may be shared with companion skills or a parent when enabled.

Mitigation: Enable records and sharing only with the student's applicable consent; use the skill's controls to view, correct, delete, pause memory, or disable sharing.

Risk: Weekly reminders rely on a separate reminder skill and may be sent through IM.

Mitigation: Queue reminders only with the student's consent and review the companion reminder skill's data and consent handling separately.

Risk: Emergency and support contacts vary by region.

Mitigation: Confirm the student's location before giving region-specific numbers and localize support channels for deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [初高中数学梯度示例](references/gradient-levels.md)
- [高一衔接数学梯度示例](references/math-hs1-gradient-levels.md)
- [高中必修后半数学梯度示例](references/math-hs2-gradient-levels.md)
- [高中选择性必修数学梯度示例](references/math-hs3-gradient-levels.md)
- [AI 生成题目自检](shared/ai-item-check.md)
- [提示阶梯](shared/hint-ladder.md)
- [危机转介与地域适配](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown]

**Output Format:** [Chinese conversational text and structured Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five-level exercises, hints, explanations, and optional progress entries tailored to the topic and grade level.]

## Skill Version(s):

2.12.5 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
