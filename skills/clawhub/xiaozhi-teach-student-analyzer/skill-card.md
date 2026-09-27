## Description:

将班级逐题测评数据转化为学情诊断、知识点弱项分析与分层教学调整建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆 K12 教师，分析班级和学生的测评数据，定位知识点弱项，并起草分层教学建议及经教师审核的家长沟通素材。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: 跨会话保存学生测评分析可能暴露未成年人信息。

Mitigation: 仅在教师认可保留记录时使用化名或学号；不需要留存时使用暂停、删除或导出控制。

Risk: 未经同意的家长沟通或学生档案写回可能泄露敏感信息。

Mitigation: 生成家长材料前确认相关分享同意，写回学生档案前确认写回同意；所有对外内容由教师审核。

Risk: 单次测评或样本不足可能导致不可靠的趋势判断与固定分层。

Mitigation: 不足三次测评时标注证据不足，不作稳定趋势判断或给学生贴长期标签。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [学情分析框架](references/analysis-framework.md)
- [班级学情报告模板](references/class-report-template.md)
- [学生个体诊断卡模板](references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Markdown reports and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [班级画像、逐题统计、知识点弱项、个体诊断和教学调整建议；可在平台支持且获得必要同意时保存去标识化分析记录。]

## Skill Version(s):

2.7.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
