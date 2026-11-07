## Description:

面向 AI 时代职业变化，帮助用户梳理职业兴趣与价值观、评估职业影响，并生成个性化职业规划报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国的学生、求职者与职场转型者，通过渐进式问答梳理兴趣、价值观和阶段目标。用于生成个性化职业方向、AI 影响评估、学习路径与行动建议。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: 保存个人职业画像或发送报告可能泄露敏感信息。

Mitigation: 将导出文件保存在私密目录；保留或发送前核对具体内容与目标位置。

Risk: 薪资估算或保险渠道推荐可能影响用户的职业或财务决策。

Mitigation: 将薪资视为估算，并独立核实保险推荐、比较其他渠道后再作决定。

Risk: 额外导出目录的宿主权限与沙箱保护未获验证。

Mitigation: 使用额外导出目录前确认宿主环境已授予相应权限。

Risk: 维护脚本在日常使用中可能造成不必要的数据变更。

Mitigation: 普通职业咨询期间不要运行随附的维护脚本。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [职业测评框架](references/assessment.md)
- [AI 对职业的影响分析](references/ai_career_impact.md)
- [薪资参考数据](references/salary_data.md)
- [保险中介机构信息披露平台](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [对话式建议与结构化 Markdown 职业规划报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [内容随用户提供的信息调整；职业、薪资和 AI 影响评级属于参考判断。]

## Skill Version(s):

2.3.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
