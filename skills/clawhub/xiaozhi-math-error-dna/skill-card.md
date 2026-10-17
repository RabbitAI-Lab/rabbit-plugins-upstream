## Description:

分析初高中数学错题的根因和反复出现的薄弱点，并在学生请求时生成弱项月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向初高中学生及其辅导者，根据错题本交接的记录细分数学错误类型、识别重复弱项，并按学生请求生成分析与月报；未经同意不建立长期档案或跨技能共享。

### Deployment Geography for Use:

面向中文 K12 数学学习场景；用于其他地区前须本地化课程、同意规则及危机求助渠道。

## Known Risks and Mitigations:

Risk: 未成年人错题与情绪数据可能在档案、跨技能交接或家长摘要中被过度共享。

Mitigation: 启用长期记忆、提醒和共享前核对学生或监护人同意设置；家长摘要须另行确认共享许可。

Risk: 非目标地区的课程、同意要求或危机求助信息可能不适用。

Mitigation: 仅在预期的中文 K12 场景直接使用；其他地区先本地化课程、同意规则与危机求助渠道。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-math-error-dna)
- [数学错误子类型表](artifact/references/math-error-dimension-table.md)
- [概念混淆图谱](artifact/references/concept-confusion-map.md)
- [读题习惯](artifact/references/reading-habits.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文文本和 Markdown 分析、弱项图谱与月报]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [历史统计依赖错题本交接；档案、提醒及家长摘要受相应同意设置约束。]

## Skill Version(s):

2.11.2 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
