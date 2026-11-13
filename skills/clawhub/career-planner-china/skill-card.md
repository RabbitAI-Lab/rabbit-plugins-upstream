## Description:

这项技能通过渐进式对话、兴趣与价值观评估以及 AI 影响分析，帮助用户制定个性化职业规划，并在用户主动要求时提供保险渠道信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向学生和职场人士，帮助他们梳理兴趣、价值观与阶段目标，比较职业方向并制定可执行的行动计划。用户明确表达保险行业兴趣或要求了解相关渠道时，也可查看独立的渠道信息。

### Deployment Geography for Use:

中国

## Known Risks and Mitigations:

Risk: 安全扫描为中等置信度且覆盖不完整，部分本地引用未能解析。

Mitigation: 安装前检查相关本地引用，并结合扫描未覆盖部分进行审阅。

Risk: 职业趋势和薪资结论来自随附的静态资料，可能无法反映最新市场情况。

Mitigation: 对影响实际选择的薪资与市场判断，使用当前的本地或官方信息复核。

Risk: 可选保险渠道清单的顺序由维护方按商业决策设定，与个性化职业适配度无关。

Mitigation: 说明排序依据，并在用户需要时并列比较其他渠道。

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [职业测评框架](references/assessment.md)
- [AI 对未来职业的影响](references/ai_career_impact.md)
- [职业锚测试参考](references/career_anchor.md)
- [MBTI 职业性格测试参考](references/mbti.md)
- [行业趋势与岗位需求](references/industry_trends.md)
- [薪资数据参考](references/salary_data.md)
- [学习路径参考](references/education_paths.md)
- [保险渠道信息](references/insurance_broker_companies.json)
- [追踪记录规则](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Files, JSON]

**Output Format:** [中文对话建议和结构化 Markdown 职业规划报告；可选 JSON 追踪记录]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [报告依据用户对话和随附静态参考资料生成；导出报告或保存追踪记录需用户明确要求。]

## Skill Version(s):

2.3.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
