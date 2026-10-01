## Description:

帮助中国大陆中小学教师按双向细目表设计试卷、题目及评分标准，并依据已有题目统计提出返修建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

供中国大陆中小学教师设计单元测验与试卷：制定双向细目表、安排难度与认知层级、生成或改编候选题和评分细则，并参考已有统计返修题目。产出须由教师审核，不提供自动判分或考后统计计算。

### Deployment Geography for Use:

中国大陆；在其他地区使用前须本地化课程、危机求助渠道及隐私要求。

## Known Risks and Mitigations:

Risk: AI 生成题可能有错、超纲或评分标准不准确。

Mitigation: 教师逐题验算答案、分值和学段适配性后，才将候选题用于正式试卷。

Risk: 输入未启用的统考试题或学生身份信息可能泄露敏感内容。

Mitigation: 不输入未启用的统考试题；使用化名或座号，不上传真实姓名、个人成绩或排名。

Risk: 在中国大陆以外沿用课程假设或危机求助号码可能误导使用者。

Mitigation: 使用前核对当地课程、隐私要求与求助渠道，并由教师审定面向学生的内容。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [试卷蓝图与评分模板](references/exam-blueprint.md)
- [AI 生成题自检协议](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文文本及 Markdown 表格]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [包含试卷蓝图、候选题、评分细则或返修清单；AI 生成题须标注并由教师逐题验算。]

## Skill Version(s):

2.9.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
